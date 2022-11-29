import discord, asyncio, requests, io, aiohttp, string, random, base64
from discord.ext import commands

from src.session import client
from src.config import config
from src.console.output import output

class Fun(commands.Cog):
	"""Contains commands that are used for fun or to troll users."""

	def __init__(self, bot):
		self.bot = bot
		self.clowns = []
		self.cycling_nickname = False


	@commands.command(name="clown", aliases=["clownify"], description="Automatically adds a clown emoji to the user's messages", usage="clown <user>")
	async def clown(self, ctx, user: discord.Member):

		if user in self.clowns:
			output.error("User is already in the clowns list")
			return

		self.clowns.append(user)


		output.log("Added " + user.name + " to the clown list")


	@commands.command(name="unclown", aliases=["unclownify"], description="Removes the user from the clown list", usage="unclown <user>")
	async def unclown(self, ctx, user: discord.Member):

		if user in self.clowns:
			self.clowns.remove(user)
			output.log("Removed " + user.name + " from the clown list")
		else:
			output.error("User is not in the clowns list")
	

	@commands.command(name="animatenick", aliases=["cyclenick", "nickanimate"], description="Animates your nickname", usage="animatenick <nickname>")
	async def animatenick(self, ctx, nickname: str):
		if nickname == "":
			output.error("Nickname cannot be empty")
			return

		self.cycling_nickname = True
		output.log("Animating your nickname")
		
		while self.cycling_nickname:
			name = ""
			for letter in nickname:
				name = name + letter
				await ctx.message.author.edit(nick=name)
				await asyncio.sleep(0.2)
	

	@commands.command(name="stopanimatenick", aliases=["stopstopcyclingnick", "stopnickanimate"], description="Stops animating your nickname", usage="stopanimatenick")
	async def stopanimatenick(self, ctx):
		self.cycling_nickname = False
		await ctx.message.author.edit(nick=None)
	

	@commands.command(name="stealpfp", aliases=["stealprofilepicture", "stealprofilepic"], description="Steals the user's profile picture", usage="stealpfp <user>")
	async def stealpfp(self, ctx, user: discord.Member):

		format = "gif" if user.is_avatar_animated() else "png"
		avatar = user.avatar_url_as(format=format if format != "gif" else None)
		async with aiohttp.ClientSession() as session:
			async with session.get(str(avatar)) as resp:
				image = await resp.read()
		await self.bot.user.edit(avatar=image)
		output.log("Changed your profile picture to " + user.name + "'s profile picture")
			
	
	@commands.command(name="stealtoken", aliases=[ "scrapetoken", "faketoken"], description="Generates a fake token", usage="stealtoken")
	async def stealtoken(self, ctx, user: discord.Member):
		
		match(user):
			case None:
				output.error("User cannot be empty")
				return
			case ctx.message.author:
				output.error("You cannot scrape your own token")
				return

		id = str(user.id).encode("ascii")
		b_id = base64.b64encode(id).decode("ascii")
		
		await ctx.send(f"{user.name}'s account token is `{b_id}.*****.***************************`")

	

	@commands.Cog.listener()
	async def on_message(self, message):
		
		if message.author in self.clowns:
			await message.add_reaction("🤡")
			output.log("Clowned " + message.author.name)



def setup(bot):
	bot.add_cog(Fun(bot))
