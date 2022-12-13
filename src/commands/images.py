import discord, requests

from discord.ext import commands
from src.console.output import output



class Images(commands.Cog):
	"""Image manipulation commands"""

	def __init__(self, bot):
		self.bot = bot
		self.image_gen_url = "https://nekobot.xyz/api/imagegen?type="


	@commands.command(name="phcomment", aliases=["phc"], description="Sends a pornhub comment with the specified text", usage="phcomment <user> <text>")
	async def phcomment(self, ctx, user: discord.Member, *, text):

		if user is None:
			user = ctx.author

		r = requests.get(f"{self.image_gen_url}phcomment&image={user.avatar_url}&text={text}&username={user.name}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")

	
	@commands.command(name="changemymind", aliases=["cmm"], description="Sends a 'change my mind' meme with the specified text", usage="changemymind <text>")
	async def changemymind(self, ctx, *, text):
		
		r = requests.get(f"{self.image_gen_url}changemymind&text={text}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")

	
	@commands.command(name="trumptweet", aliases=["tt"], description="Sends a trump tweet with the specified text", usage="trumptweet <text>")
	async def trumptweet(self, ctx, *, text):
		
		r = requests.get(f"{self.image_gen_url}trumptweet&text={text}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")

	
	@commands.command(name="tweet", aliases=["tw"], description="Sends a tweet with the specified text", usage="tweet <user> <text>")
	async def tweet(self, ctx, user: discord.Member, *, text):
		
		if user is None:
			user = ctx.author

		r = requests.get(f"{self.image_gen_url}tweet&username={user.name}&text={text}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")
	

	@commands.command(name="clyde", aliases=["cl"], description="Sends a clyde message with the specified text", usage="clyde <text>")
	async def clyde(self, ctx, *, text):
		
		r = requests.get(f"{self.image_gen_url}clyde&text={text}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")

	
	@commands.command(name="trash", aliases=["t"], description="Sends a trash image with the specified user", usage="trash <user>")
	async def trash(self, ctx, user: discord.Member):
		
		if user is None:
			user = ctx.author

		r = requests.get(f"{self.image_gen_url}trash&url={user.avatar_url}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")


	@commands.command(name="captcha", aliases=["c"], description="Sends a captcha image with the specified user", usage="captcha <user>")
	async def captcha(self, ctx, user: discord.Member):

		if user is None:
			user = ctx.author

		r = requests.get(f"{self.image_gen_url}captcha&url={user.avatar_url}&username={user.name}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")

	
	@commands.command(name="ship", aliases=["s"], description="Sends a ship image with the specified users", usage="ship <user1> <user2>")
	async def ship(self, ctx, user1: discord.Member, user2: discord.Member):

		if user1 is None:
			user1 = ctx.author

		if user2 is None:
			user2 = ctx.author

		r = requests.get(f"{self.image_gen_url}ship&user1={user1.avatar_url}&user2={user2.avatar_url}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")

	
	@commands.command(name="threats", aliases=["th"], description="Sends a threats image with the specified user", usage="threats <user>")
	async def threats(self, ctx, user: discord.Member):
		
		if user is None:
			user = ctx.author

		r = requests.get(f"{self.image_gen_url}threats&url={user.avatar_url}")

		if r.status_code == 200:
			await ctx.send(r.json()["message"])

		else:
			output.error(f"Error: {r.status_code} {r.reason}")



def setup(bot):
	bot.add_cog(Images(bot))
