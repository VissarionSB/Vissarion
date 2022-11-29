import discord
from discord.ext import commands

from src.commands.utils.message_builder import builder
from src.session import client
from src.config import config
from src.console.output import output

class Help(commands.Cog):
	"""Help menus"""

	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="help", aliases=["helpmenu", "cmds", "commands"], description="Sends the help menu", usage="help")
	async def help(self, ctx):

		prefix = client.prefix

		menu = f"""
<quote><bold>Categories<reset><nl><quote><nl>

<field>
	<col_purple>{prefix}<reset>user
	<content>
		Lets you manipulate your discord user	
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>hashes
	<content>
		Various hashing utilities
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>settings
	<content>
		Bot settings
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>misc
	<content>
		Miscellaneous
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>exploits
	<content>
		Exploits or something
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>raiding
	<content>
		Basic raiding utility
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>fun
	<content>
		Fun and trollin'
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>dumping
	<content>
		Dumping utility
	</content>
</field>

<field>
	<col_purple>{prefix}<reset>spotify
	<content>
		Spotify spoof
	</content>
</field>
		"""
		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)	


	@commands.command(name="user", aliases=["account"], description="Sends the user help menu", usage="user <page>")
	async def user(self, ctx, page: int=1):

		contents = [""]
		content = ""

		cog = self.bot.get_cog('User')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			if(len(content) < 500):
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""

			else:
				contents.append(content)
				content = ""

		pages = (len(contents) - 1)

		if(page == 0 or page > pages):
			output.error("Invalid page number. Number of pages:", separated_text=str(len(contents) - 1))
			return
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{contents[page]}
<quote><nl>
<quote>Page » {page}/{pages}<nl>"""
		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)


	@commands.command(name="hashes", aliases=["encryption"], description="Sends the hashes help menu", usage="hashes <page>")
	async def hashes(self, ctx, page: int=1):

		contents = [""]
		content = ""

		cog = self.bot.get_cog('Hashes')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			if(len(content) < 500):
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""

			else:
				contents.append(content)
				content = ""

		pages = (len(contents) - 1)

		if(page == 0 or page > pages):
			output.error("Invalid page number. Number of pages:", separated_text=str(len(contents) - 1))
			return
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{contents[page]}
<quote><nl>
<quote>Page » {page}/{pages}<nl>"""
		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)


	@commands.command(name="settings", aliases=[], description="Sends the settings help menu", usage="settings <page>")
	async def settings(self, ctx, page: int=1):

		contents = [""]
		content = ""

		cog = self.bot.get_cog('Settings')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			if(len(content) < 400):
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""

			else:
				contents.append(content)
				content = ""

		pages = (len(contents) - 1)

		if(page == 0 or page > pages):
			output.error("Invalid page number. Number of pages:", separated_text=str(len(contents) - 1))
			return
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{contents[page]}
<quote><nl>
<quote>Page » {page}/{pages}<nl>"""
		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)


	@commands.command(name="misc", aliases=[], description="Sends the misc help menu", usage="misc <page>")
	async def misc(self, ctx, page: int=1):

		contents = [""]
		content = ""

		cog = self.bot.get_cog('Misc')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			if(len(content) < 500):
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""

			else:
				contents.append(content)
				content = ""

		pages = (len(contents) - 1)

		if(page == 0 or page > pages):
			output.error("Invalid page number. Number of pages:", separated_text=str(len(contents) - 1))
			return
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{contents[page]}
<quote><nl>
<quote>Page » {page}/{pages}<nl>"""

		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)


	@commands.command(name="spotify", aliases=[], description="Sends the spotify help menu", usage="spotify <page>")
	async def spotify(self, ctx, page: int=1):

		contents = [""]
		content = ""

		cog = self.bot.get_cog('Spotify')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			if(len(content) < 300):
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""

			else:
				contents.append(content)
				content = ""

		pages = (len(contents) - 1)

		if(page == 0 or page > pages):
			output.error("Invalid page number. Number of pages:", separated_text=str(len(contents) - 1))
			return
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{contents[page]}
<quote><nl>
<quote>Page » {page}/{pages}<nl>"""
		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)


	@commands.command(name="raiding", aliases=[], description="Sends the raiding help menu", usage="raiding <page>")
	async def raiding(self, ctx, page: int=1):

		content = ""

		cog = self.bot.get_cog('Raiding')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			content += f"""
			<field>
				<col_purple>{prefix}<reset>{command.usage}
				<content>
					{command.description:<17}
				</content>
			</field>
			"""

		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{content}
<quote><nl>"""

		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)



	@commands.command(name="networking", aliases=[], description="Sends the networking help menu", usage="networking <page>")
	async def networking(self, ctx, page: int=1):

		content = ""

		cog = self.bot.get_cog('Networking')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			content += f"""
			<field>
				<col_purple>{prefix}<reset>{command.usage}
				<content>
					{command.description:<17}
				</content>
			</field>
			"""
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{content}
<quote><nl>"""

		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)



	@commands.command(name="fun", aliases=[], description="Sends the fun help menu", usage="fun <page>")
	async def fun(self, ctx, page: int=1):

		contents = [""]
		content = ""

		cog = self.bot.get_cog('Fun')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			if(len(content) < 500):
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""

			else:
				contents.append(content)
				content = ""

		pages = (len(contents) - 1)

		if(page == 0 or page > pages):
			output.error("Invalid page number. Number of pages:", separated_text=str(len(contents) - 1))
			return
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{contents[page]}
<quote><nl>
<quote>Page » {page}/{pages}<nl>"""

		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)



	@commands.command(name="exploits", aliases=[], description="Sends the exploits help menu", usage="exploits <page>")
	async def exploits(self, ctx, page: int=1):

		content = ""

		cog = self.bot.get_cog('Exploits')
		commands = cog.get_commands()

		prefix = client.prefix

		for command in commands:
			content += f"""
			<field>
				<col_purple>{prefix}<reset>{command.usage}
				<content>
					{command.description:<17}
				</content>
			</field>
			"""
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{content}
<quote><nl>"""

		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)



	@commands.command(name="dumping", aliases=[], description="Sends the dumping help menu", usage="dumping <page>")
	async def dumping(self, ctx, page: int=1):

		content = ""

		cog = self.bot.get_cog('Dumping')
		commands = cog.get_commands()

		prefix = client.prefix
		for command in commands:
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{content}
<quote><nl>"""

		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)


	@commands.command(name="listall", aliases=[], description="Lists all commands", usage="listall <page>")
	async def listall(self, ctx, page: int=1):

		contents = [""]
		content = ""

		prefix = client.prefix

		for command in self.bot.commands:
			if(len(content) < 800):
				content += f"""
				<field>
					<col_purple>{prefix}<reset>{command.usage}
					<content>
						{command.description:<17}
					</content>
				</field>
				"""

			else:
				contents.append(content)
				content = ""

		pages = (len(contents) - 1)

		if(page == 0 or page > pages):
			output.error("Invalid page number. Number of pages:", separated_text=str(len(contents) - 1))
			return
		
		menu = f"""
<quote><bold>Commands<reset><nl><quote><nl>

{contents[page]}
<quote><nl>
<quote>Page » {page}/{pages}<nl>"""

		await ctx.send(builder.message(str(ctx.command.name), menu), delete_after=client.delete_after)


def setup(bot):
	bot.add_cog(Help(bot))

#todo
#also refactorte