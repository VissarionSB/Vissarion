import discord, os, requests, asyncio, sys
from discord.ext import commands

from src.config import config
config.init()

from src.session import client
from src.console.output import output
from src.modules.sessions_manager import sessions_manager


#hide le cursor
if (sys.platform == "linux"):
	os.system("tput civis")


"""Initializes the bot."""
bot = commands.Bot(command_prefix=config.read()['commands']['prefix'], self_bot=True, caseinsensitive=True)
bot.remove_command("help")





def warn(*args, **kwargs):
	pass


async def cog_setup():
	"""Loads all cogs."""

	for command_file in os.listdir("./src/commands"):
		if command_file.endswith(".py"):
			bot.load_extension(f"src.commands.{command_file[:-3]}")


async def startup_state():
	"""Sets the bot's status."""
	
	await asyncio.sleep(3) # <~ Wait so the bot connects properly and doesn't interrupt any of these.

	if(config.read()["startup_state"]["enabled"] == True):
		output.log("Set up startup state")

		match (config.read()["startup_state"]["activity"]):
			case "playing":
				await bot.change_presence(activity=discord.Game(name=config.read()["startup_state"]["activity_name"]))
			case "streaming":
				await bot.change_presence(activity=discord.Streaming(name=config.read()["startup_state"]["activity_name"], url=config.read()["startup_state"]["stream_url"]))
			case "listening":
				await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=config.read()["startup_state"]["activity_name"]))
			case "watching":
				await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config.read()["startup_state"]["activity_name"]))
			case "null":
				pass

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}
		
		if(config.read()["startup_state"]["custom_status"] != "null"):
	
			payload = {
				"custom_status": {	
					"text": config.read()["startup_state"]["custom_status"]
				}
			}
			
			requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
	
		if(config.read()["startup_state"]["status"] != "null"):

			payload = {
				"status": config.read()["startup_state"]["status"]
			}

			r = requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=payload)


@bot.event
async def on_connect():
	"""Starts up most of the bot's functionality when you connect to discord."""
	
	output.clear()
	output.print_banner("Connected", str(bot.user), str(bot.command_prefix))
	output.title("Vissarion")
	bot.loop.create_task(sessions_manager.check_sessions())
	output.log_sessions("Initialized the session manager")

	client.start_rpc()

	await cog_setup()
	await startup_state()


@bot.before_invoke
async def before_invoke(ctx):
	"""Logs the command before it's invoked, checks the config and deletes invoking"""

	config._check()
	if(config.read()['commands']['delete_invoking']):
		try:
			await ctx.message.delete()
		except:
			pass

	output.cmd(str(ctx.command.name))


@bot.event
async def on_command(ctx):
	"""Handler"""
	pass


@bot.event
async def on_command_error(ctx, error):
	"""Handles errors that occur when a command is used incorrectly."""
	
	match(type(error)):

		case commands.CommandNotFound:
			output.error(f"Command not found:", separated_text = str(ctx.invoked_with))
			pass

		case commands.MissingRequiredArgument:
			output.error("Missing required argument(s) <~ valid usage:", separated_text = str(ctx.command.usage))
			pass

		case commands.BadArgument:
			output.error("Invalid argument(s) <~ valid usage:", separated_text = str(ctx.command.usage))
			pass
		
		case commands.MissingPermissions:
			output.error("Missing permissions <~ ", separated_text = str(ctx.invoked_with))


client.connect(bot)
