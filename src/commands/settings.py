import discord
from discord.ext import commands

from src.config import config
from src.console.output import output



class Settings(commands.Cog):
	"""Contains commands that are used to change the bot's settings."""

	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="setcommandmode", aliases=["commandmode", "cmode"], description="Changes the command mode to the selected one", usage="setcommandmode <mode>")
	async def setcommandmode(self, ctx, mode: str):
		modes = ['embed', 'ansi']

		if mode in modes:
			config.save_key("commands", mode, subkey="command_mode")
			output.log("Command mode set to " + mode)
		else:
			output.error("Invalid mode. Valid modes <~ ", separated_text="embed, ansi")


	@commands.command(name="setconsolecolors", aliases=["consolecolors", "ccolors"], description="Changes the console colors to the selected one", usage="setconsolecolors <primary> <secondary>")
	async def setconsolecolors(self, ctx, primary: str, secondary: str):
		
		config.save_key("console", primary, subkey="primary_color")
		config.save_key("console", secondary, subkey="secondary_color")
		output.log("Console colors set to " + primary + " and " + secondary)
		output.refresh(str(self.bot.user), str(self.bot.command_prefix))


	@commands.command(name="prefix", aliases=["setprefix"], description="Changes the bot's prefix", usage="prefix <prefix>")
	async def prefix(self, ctx, prefix: str):
		config.save_key("commands", prefix, subkey="prefix")
		
		self.bot.command_prefix = prefix

		client._refresh_prefix()
		output.refresh(str(self.bot.user), str(self.bot.command_prefix))
		output.log("Prefix set to " + prefix)


	@commands.command(name="setrpc", aliases=[], description="Changes the bot's rpc", usage="setrpc <setting> <value>")
	async def setrpc(self, ctx, setting: str, value: str):
		settings = ['client_id', 'details', 'state', 'large_image', 'large_text', 'small_image', 'small_text']

		if setting in settings:
			config.save_key("rich_presence", value, subkey=setting)
			output.log("Rich presence's" + setting + " has been set to " + value)
		else:
			output.error("Invalid setting. Valid settings <~ ", separated_text="details, state, large_image, large_text, small_image, small_text")
	

	@commands.command(name="rpc", aliases=[], description="Toggles rpc", usage="rpc")
	async def rpc(self, ctx):
		data = config.read()
		data["rich_presence"]["enabled"] = not config["rich_presence"]["enabled"]
		config.save(data)

		output.log("Rich presence has been " + ("enabled" if data["rich_presence"]["enabled"] else "disabled"))
	
	
	@commands.command(name="setembed", aliases=["embed"], description="Changes the embed", usage="setembed <setting> <value>")
	async def setembed(self, ctx, setting: str, value: str):

		settings = ['host', 'title', 'description', 'image_url','color', 'footer', 'large']
		allowed_hosts = ['vaul.xyz']

		if setting in settings:
			if setting == "host":
				if value in allowed_hosts:
					config.save_key("embeds", value, subkey=setting)
					output.log("Embed's host has been set to " + value)
				else:
					output.error("Invalid host. Valid hosts <~ ", separated_text="vaul.xyz, rauf.wtf")
				
			else:
				config.save_key("embed", value, subkey=setting)
				output.log("Embed's " + setting + " has been set to " + value)
		else:
			output.error("Invalid setting. Valid settings <~ ", separated_text="color, title, description, footer, thumbnail, image, author")


	@commands.command(name="setansi", aliases=["ansi"], description="Changes the ansi", usage="setansi <setting> <value>")
	async def setansi(self, ctx, setting: str, value: str):
		
		settings = ['title', 'footer']

		if setting in settings:
			config.save_key("ansi", value, subkey=setting)
			output.log("Ansi's " + setting + " has been set to " + value)
		else:
			output.error("Invalid setting. Valid settings <~ ", separated_text="color, title, description, footer, thumbnail, image, author")


	@commands.command(name="setsessionmanager", aliases=["ssm"], description="Changes the session manager", usage="setsessionmanager <setting> <value>")
	async def setsessionmanager(self, ctx, setting: str, value: str):
		
		settings = ['operating_systems', 'platforms', 'locations']
	
		if setting in settings:
			data = config.read()
			data['session_manager'][setting].append(value)

			config.save(data)
			output.log(f"{value} has been added to {setting} in the session manager's whitelist")
		else:

			output.log("Invalid setting. Valid settings <~ ", separated_text="operating_systems, platforms, locations")
	

	@commands.command(name="sessionmanager", aliases=["sm"], description="Toggles the session manager", usage="sessionmanager")
	async def sessionmanager(self, ctx):

		data = config.read()
		data["session_manager"]["enabled"] = not config["session_manager"]["enabled"]
		config.save(data)

		output.log("Session manager has been " + ("enabled" if data["session_manager"]["enabled"] else "disabled"))
	

	@commands.command(name="setstartupstate", aliases=["startupstate"], description="Changes the startup state", usage="setstartupstate <setting> <value>")
	async def setstartupstate(self, ctx, setting: str, value: str):
		
		activites = ['playing', 'streaming', 'listening', 'watching', 'null']
		statuses = ['online', 'idle', 'dnd', 'invisible']
		settings = ['activity', 'activity_name', 'status', 'custom_status', 'stream_url']

		if setting in settings:
			match(setting):
				case "activity":
					if value in activites:
						config.save_key("startup_state", value, subkey=setting)
						output.log("Startup state's activity has been set to " + value)
					else:
						output.error("Invalid activity. Valid activities <~ ", separated_text="playing, streaming, listening, watching, null")
				case "status":
					if value in statuses:
						config.save_key("startup_state", value, subkey=setting)
						output.log("Startup state's status has been set to " + value)
					else:
						output.error("Invalid status. Valid statuses <~ ", separated_text="online, idle, dnd, invisible")
				case _:
					config.save_key("startup_state", value, subkey=setting)
					output.log("Startup state's " + setting + " has been set to " + value)
		else:
			output.error("Invalid setting. Valid settings <~ ", separated_text="activity, activity_name, status, custom_status, stream_url")
	#TODO
	#refactor shit above using config_image easily doable


	@commands.command(name="setstartup", aliases=["startup"], description="Toggles the startup state", usage="setstartup")
	async def setstartup(self, ctx):

		data = config.read()
		data["startup_state"]["enabled"] = not config["startup_state"]["enabled"]
		config.save(data)

		output.log("Startup state has been " + ("enabled" if data["startup_state"]["enabled"] else "disabled"))

	

def setup(bot):
	bot.add_cog(Settings(bot))
