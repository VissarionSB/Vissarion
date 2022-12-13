import discord, asyncio, requests, aiohttp, string, random, base64
from discord.ext import commands

from src.console.output import output



class Fun(commands.Cog):
	"""Contains commands that are used for fun or to troll users."""

	def __init__(self, bot):
		self.bot = bot
		self.clowns = []
		self.mocking = []
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
	
	
	@commands.command(name="mock", aliases=[], description="Automatically responds to a user's message with a mocked version", usage="mock <user>")
	async def mock(self, ctx, user: discord.Member):
		if user in self.mocking:
			output.error("User is already being mocked")
			return

		self.mocking.append(user)
		output.log("Started mocking " + user.name)


	@commands.command(name="unmock", aliases=[], description="Stops mocking a user", usage="unmock <user>")
	async def unmock(self, ctx, user: discord.Member):

		if user in self.mocking:
			self.mocking.remove(user)
			output.log("Stopped mocking " + user.name)
		else:
			output.error("User is not being mocked")


	@commands.command(name="minesweeper", aliases=["mines"], description="Generates a minesweeper board", usage="minesweeper <width> <height> <mines>")
	async def minesweeper(self, ctx, width: int = 5, height: int = 5, mines: int = 4):
		
		if width > 10 or height > 10:
			output.error("Width and height cannot be greater than 10")
			return

		if mines > width * height:
			output.error("The amount of mines cannot be greater than the amount of tiles")
			return

		board = []

		for x in range(width):
			board.append([])
			for y in range(height):
				board[x].append("||:white_large_square:||")

		for x in range(mines):
			while True:
				x = random.randint(0, width - 1)
				y = random.randint(0, height - 1)
				if board[x][y] != "||:bomb:||":
					board[x][y] = "||:bomb:||"
					break

		for x in range(width):
			for y in range(height):
				if board[x][y] != "||:bomb:||":
					adjacent_mines = 0
					for x2 in range(-1, 2):
						for y2 in range(-1, 2):
							if x + x2 >= 0 and x + x2 < width and y + y2 >= 0 and y + y2 < height:
								if board[x + x2][y + y2] == "||:bomb:||":
									adjacent_mines += 1
					if adjacent_mines != 0:
						adjacent_mines = {
							1: "one",
							2: "two",
							3: "three",
							4: "four",
							5: "five",
							6: "six",
							7: "seven",
							8: "eight"
						}[adjacent_mines]

						board[x][y] = f"||:{adjacent_mines}:||"

		board_string = ""

		for x in range(width):
			for y in range(height):
				board_string += board[x][y]
			board_string += "\n"
	
		await ctx.send(board_string)


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
		
		if message.author in self.mocking:
			def mock(msg) -> str:
				mocked = ""
				i = True
				for char in msg:
					if i:
						mocked += char.upper()
					else:
						mocked += char.lower()
					if char != ' ':
						i = not i
				return mocked
			await message.reply(mock(message.content))



def setup(bot):
	bot.add_cog(Fun(bot))
