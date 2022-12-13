import discord, requests
from discord.ext import commands

from src.session import client
from src.console.output import output
from src.config import config



class User(commands.Cog):
	"""Contains commands that are used to manipulate your user account."""

	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="darkmode", aliases=["setdarkmode", "darktheme"], description="Changes your discord theme to dark", usage="darkmode")
	async def darkmode(self, ctx):

		payload = {
			"theme": "dark"
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)


	@commands.command(name="lightmode", aliases=["setlightmode", "lighttheme"], description="Changes your discord theme to light", usage="lightmode")
	async def lightmode(self, ctx):

		payload = {
			"theme": "light"
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}
		
		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)


	@commands.command(name="setdiscordtheme", aliases=["discordtheme", "dtheme"], description="Changes your discord theme to the selected one", usage="setdiscordtheme <theme>")
	async def setdiscordtheme(self, ctx, theme: str):
		themes = ['light', 'dark']

		if theme in themes:
			payload = {
				"theme": theme
			}

			headers = {
				"Authorization": client.token,
				"Content-Type": "application/json"
			}

			requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
		else:
			output.error("Invalid theme. Valid themes <~ ", separated_text="light, dark")
		   

	@commands.command(name="hypesquad", aliases=["changehypesquad", "sethypesquad"], description="Changes your hypesquad", usage="hypesquad <house>")
	async def hypesquad(self, ctx, house: str):

		houses = {
			"bravery": 1,
			"brilliance": 2, 
			"balance": 3
		}

		if house in list(houses.keys()):
			payload = {
				"house_id": houses[house]
			}

			headers = {
				"Authorization": client.token,
				"Content-Type": "application/json"
			}

			r = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)

		else:
			output.error("Invalid house. Valid houses <~ ", separated_text="bravery, brilliance, balance")


	@commands.command(name="online", aliases=["setonline"], description="Sets your discord status to online", usage="online")
	async def online(self, ctx):
		
		payload = {
			"status": "online"
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)


	@commands.command(name="idle", aliases=["setidle"], description="Sets your discord status to idle", usage="idle")
	async def idle(self, ctx):
		
		payload = {
			"status": "idle"
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
	

	@commands.command(name="dnd", aliases=["setdnd"], description="Sets your discord status to dnd", usage="dnd")
	async def dnd(self, ctx):
		
		payload = {
			"status": "dnd"
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
		

	@commands.command(name="invisible", aliases=["setinvisible", "offline"], description="Sets your discord status to invisible", usage="invisible")
	async def invisible(self, ctx):
		
		payload = {
			"status": "invisible"
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
	

	@commands.command(name="setstatus", aliases=[], description="Sets your discord status to the provided one", usage="setstatus <status>")
	async def setstatus(self, ctx, status: str):

		statuses = ['online', 'idle', 'dnd', 'invisible']

		if status in statuses:

			payload = {
				"status": status
			}

			headers = {
				"Authorization": client.token,
				"Content-Type": "application/json"
			}

			requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
		else:
			output.error("Invalid status. Valid statuses <~ ", separated_text="online, idle, dnd, invisible")


	@commands.command(name="playing", aliases=["setplaying"], description="Sets your discord activity to playing", usage="playing <game>")
	async def playing(self, ctx, *, game: str):
		await self.bot.change_presence(activity=discord.Game(name=game))


	@commands.command(name="streaming", aliases=["setstreaming"], description="Sets your discord activity to streaming", usage="streaming <game>")
	async def streaming(self, ctx, *, game: str):
		await self.bot.change_presence(activity=discord.Streaming(name=game, url=config.read()["startup_state"]["stream_url"]))
	

	@commands.command(name="listening", aliases=["setlistening"], description="Sets your discord activity to listening", usage="listening <game>")
	async def listening(self, ctx, *, name: str):
		await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))


	@commands.command(name="watching", aliases=["setwatching"], description="Sets your discord activity to watching", usage="watching <game>")
	async def watching(self, ctx, *, name: str):
		await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
	

	@commands.command(name="setactivity", aliases=["activity"], description="Sets your discord activity to the provided one", usage="setactivity <activity> <name>")
	async def setactivity(self, ctx, activity: str, name:str):
		
		activities = ['playing', 'streaming', 'listening', 'watching']

		if activity in activities:

			match(activity):

				case "playing":
					await self.bot.change_presence(activity=discord.Game(name=name))
		
				case "streaming":
					await self.bot.change_presence(activity=discord.Streaming(name=name, url=config.read()["startup_status"]["stream_url"]))
				
				case "listening":
					await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
				
				case "watching":
					await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
					
		else:
			output.error("Invalid activity. Valid activities <~ ", separated_text="playing, streaming, listening, watching")

	
	@commands.command(name="setcustomstatus", aliases=["cstatus", "customstatus"], description="Sets your custom status to the provided one", usage="setcustomstatus <emoji> <text>")
	async def setcustomstatus(self, ctx, emoji: str, *, text: str):

		payload = {
			"custom_status": {
				"text": text,
				"emoji_name": emoji
			}
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)


	@commands.command(name="clearcustomstatus", aliases=["ccstatus", "clearcstatus"], description="Clears your custom status", usage="clearcustomstatus")
	async def clearcustomstatus(self, ctx):

		payload = {
			"custom_status": {
				"text": "",
				"emoji_name": ""
			}
		}

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)


	@commands.command(name="clearactivity", aliases=["cleanactivity"], description="Clears your discord activity", usage="clearactivity")
	async def clearactivity(self, ctx):
		await self.bot.change_presence(activity=None)


	@commands.command(name="setnickname", aliases=["nickname", "nick", "setnick"], description="Sets your nickname to the provided one", usage="setnickname <nickname>")
	async def setnickname(self, ctx, *, nickname: str):
		await ctx.message.author.edit(nick=nickname)


	@commands.command(name="clearnickname", aliases=["cleannickname", "clearnick", "cleannick"], description="Clears your nickname", usage="clearnickname")
	async def clearnickname(self, ctx):
		await ctx.message.author.edit(nick=None)



def setup(bot):
	bot.add_cog(User(bot))

#todo 
#refactor this shit
