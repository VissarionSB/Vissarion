import discord, discord_rpc, discum, os, ast, requests, json, time
from discord.ext import commands

from src.commands.utils.message_builder import builder
from src.session import client
from src.console.output import output
from src.globals import global_vars
from src.config import config



class Misc(commands.Cog):
	"""Contains some uncategorized commands."""

	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="userinfo", aliases=["whois"], description="Shows information about a user", usage="userinfo <user>")
	async def userinfo(self, ctx, user: discord.Member=None):

		if user == None:
			user = ctx.author

		message = f"""
<field>
	<bold>Username<reset>
	<content>
		{user.name}
	</content>
</field>
<field>
	<col_purple>Discriminator<reset>
	<content>
		{user.discriminator}
	</content>
</field>
<quote><nl>
<field>
	Id
	<content>
		{user.id}
	</content>
</field>
<field>
	Status
	<content>
		{user.status}
	</content>
</field>
<field>
	Activity
	<content>
		{user.activity}
	</content>
</field>
<field>
	Created at
	<content>
		{user.created_at.strftime('%m/%d/%Y | %H:%M:%S')}
	</content>
</field>
<field>
	Joined at
	<content>
		{user.joined_at.strftime('%m/%d/%Y | %H:%M:%S')}
	</content>
</field>
"""

	
		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)


	@commands.command(name="serverinfo", aliases=["guildinfo"], description="Shows information about the server", usage="serverinfo")
	async def serverinfo(self, ctx):
		
		message = f"""
<field>
	<bold>Name<reset>
	<content>
		{ctx.guild.name}
	</content>
</field>
<field>
	<col_purple>Id<reset>
	<content>
		{ctx.guild.id}
	</content>
</field>
<quote><nl>
<field>
	Owner
	<content>
		{ctx.guild.owner}
	</content>
</field>
<field>
	Region
	<content>
		{ctx.guild.region}
	</content>
</field>
<field>
	Created at
	<content>
		{ctx.guild.created_at.strftime('%m/%d/%Y | %H:%M:%S')}
	</content>
</field>
<field>
	Members
	<content>
		{ctx.guild.member_count}
	</content>
</field>
<field>
	Channels
	<content>
		{len(ctx.guild.channels)}
	</content>
</field>
<field>
	Roles
	<content>
		{len(ctx.guild.roles)}
	</content>
</field>
<field>
	Emojis
	<content>
		{len(ctx.guild.emojis)}
	</content>
</field>
<field>
	Boosts
	<content>
		{ctx.guild.premium_subscription_count}
	</content>
</field>
<field>
	Boost tier
	<content>
		{ctx.guild.premium_tier}
	</content>
</field>
<field>
	Verification level
	<content>
		{ctx.guild.verification_level}
	</content>
</field>"""
		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)


	@commands.command(name="avatar", description="Shows a user's avatar", usage="avatar <user>")
	async def avatar(self, ctx, user: discord.Member=None):
		
		if user == None:
			user = ctx.author

		await ctx.send(user.avatar_url, delete_after=client.delete_after)


	@commands.command(name="webhookinfo", aliases=["webhook"], description="Gets information about a webhook", usage="webhookinfo <webhook_id>")
	async def webhookinfo(self, ctx, webhook_id: str):
		try:
			webhook = await self.bot.fetch_webhook(webhook_id)
		except:
			output.log(f"Invalid webhook")
			return

		message = f"""
<field>
	<bold>Name<reset>
	<content>
		{webhook.name}
	</content>
</field>
<field>
	<col_purple>Id<reset>
	<content>
		{webhook.id}
	</content>
</field>
<quote><nl>
<field>
	Guild
	<content>
		{webhook.guild}
	</content>
</field>
<field>
	Channel
	<content>
		{webhook.channel}
	</content>
</field>
<field>
	Avatar
	<content>	
		{webhook.avatar_url}
	</content>
</field>
<field>
	Token
	<content>
		{webhook.token}
	</content>
</field>
<field>
	Created at
	<content>
		{webhook.created_at.strftime('%m/%d/%Y | %H:%M:%S')}
	</content>
</field>
<field>
	Type
	<content>	
		{webhook.type}
	</content>
</field>
<field>
	Url
	<content>
		{webhook.url}
	</content>
</field>
"""		
		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)


	@commands.command(name="selfpurge", aliases=['spurge', 'sp'], description="Deletes a specified amount of messages", usage="purge <amount>")
	async def selfpurge(self, ctx, amount: int):
		async for message in ctx.message.channel.history(limit=amount).filter(lambda message: message.author == self.bot.user).map(lambda m: m):
			try:
				await message.delete()
			except:
				pass

		output.log(f"Purged {amount} messages on {ctx.channel} in {ctx.guild.name}")


	@commands.command(name="purge", aliases=['prune'], description="Deletes a specified amount of messages", usage="purge <amount>")
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx, amount: int):
		await ctx.channel.purge(limit=amount)
		output.log(f"Purged {amount} messages on {ctx.channel} in {ctx.guild.name}")


	@commands.command(name="parse", description="Parses a message", usage="parse <message>")
	async def parse(self, ctx, *, message):
		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)
	

	@commands.command(name="parsefromfile", description="Parses a message from a file", usage="parsefromfile <file>")
	async def parsefromfile(self, ctx, file):

		if os.path.exists(os.path.expanduser("~/vissarion/parser_files/" + file)):
			with open(os.path.expanduser("~/vissarion/parser_files/") + file, "r") as f:
				message = f.read()
			await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)
		else:
			output.error("File not found")


	@commands.command(name="ping", description="Shows the bot's ping", usage="ping")
	async def ping(self, ctx):
		await ctx.send(f"{round(self.bot.latency * 1000)}ms", delete_after=client.delete_after)
	

	@commands.command(name="uptime", description="Shows the bot's uptime", usage="uptime")
	async def uptime(self, ctx):
		output.log(f"{round(time.time() - self.bot.start_time)}s")
	
	
	@commands.command(name="eval", description="Evaluates a python expression", usage="eval <expression>")
	async def eval(self, ctx, *, expression):
			
		def _insert_returns(body):
			
			if isinstance(body[-1], ast.Expr):
				body[-1] = ast.Return(body[-1].value)
				ast.fix_missing_locations(body[-1])
			if isinstance(body[-1], ast.If):
				insert_returns(body[-1].body)
				insert_returns(body[-1].orelse)
			if isinstance(body[-1], ast.With):
				insert_returns(body[-1].body)

		fn_name = "_eval_expr"
		expression = expression.strip("` ")
	
		expression = "\n".join(f"    {i}" for i in expression.splitlines())
	
		body = f"async def {fn_name}():\n{expression}"
	
		parsed = ast.parse(body)
		body = parsed.body[0].body
	
		_insert_returns(body)
	
		env = {
			'bot': ctx.bot,
			'discord': discord,
			'commands': commands,
			'ctx': ctx,
			'__import__': __import__
		}

		exec(compile(parsed, filename="<ast>", mode="exec"), env)
	
		result = (await eval(f"{fn_name}()", env))
		await ctx.send(result, delete_after=client.delete_after)

		#https://gist.github.com/simmsb/2c3c265813121492655bc95aa54da6b9
	

	@commands.command(name="reload", description="Reloads a cog", usage="reload <cog>")
	async def reload(self, ctx, cog):
		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
			await output.log(f"Reloaded {cog}")
		except Exception as err:
			await output.log(f"Failed to reload {cog} | {err}")
			pass

	
	@commands.command(name="load", description="Loads a cog", usage="load <cog>")
	async def load(self, ctx, cog):
		try:
			self.bot.load_extension(cog)
			await output.log(f"Loaded {cog}")
		except Exception as err:
			await output.log(f"Failed to load {cog} | {err}")
			pass

	
	@commands.command(name="unload", description="Unloads a cog", usage="unload <cog>")
	async def unload(self, ctx, cog):
		try:
			self.bot.unload_extension(cog)
			await output.log(f"Unloaded {cog}")
		except Exception as err:
			await output.log(f"Failed to unload {cog} | {err}")
			pass
	

	@commands.command(name="reloadall", description="Reloads all cogs", usage="reloadall")
	async def reloadall(self, ctx):
		for cog in self.bot.extensions:
			try:
				self.bot.unload_extension(cog)
				self.bot.load_extension(cog)
				await output.log(f"Reloaded {cog}")
			except Exception as err:
				await output.log(f"Failed to reload {cog} | {err}")
				pass

	
	@commands.command(name="loadall", description="Loads all cogs", usage="loadall")
	async def loadall(self, ctx):
		for command_file in os.listdir("/"):
			if command_file.endswith(".py"):
				try:
					self.bot.load_extension(f"{command_file[:-3]}")
					await output.log(f"Loaded {command_file}")
				except Exception as err:
					await output.log(f"Failed to load {command_file} | {err}")
					pass


	@commands.command(name="unloadall", description="Unloads all cogs", usage="unloadall")
	async def unloadall(self, ctx):

		for cog in self.bot.extensions:
			try:
				self.bot.unload_extension(cog)
				await output.log(f"Unloaded {cog}")
			except Exception as err:
				await output.log(f"Failed to unload {cog} | {err}")
				pass

	
	@commands.command(name="savebackup", description="Saves a backup of your discord account", usage="savebackup (name)")
	async def savebackup(self, ctx, name):
	
		discum_client = discum.Client(token=client.token, log=False, user_agent=client.get_random_useragent())
		
		if not os.path.exists(os.path.expanduser(f"{global_vars.user_info['config_path']}/backups/" + name)):
			os.makedirs(os.path.expanduser(f"{global_vars.user_info['config_path']}/backups/" + name))
	
		data = {
			"main_user": {
				"username": ctx.author.name,
				"discriminator": ctx.author.discriminator,
				"id": ctx.author.id,
				"avatar": str(ctx.author.avatar_url),
			},
			"friends": [],
			"blocked_users": [],
			"outgoing_requests": [],
			"incoming_requests": [],
			'guilds': []
		}

		headers = {
			"Authorization": client.token
		}

		relationships = requests.get("https://discord.com/api/v10/users/@me/relationships", headers=headers)
		relationships_data = relationships.json()

		for entry in relationships_data:
			match entry["type"]:
				case 1:
					data["friends"].append({"username": entry["user"]["username"] + "#" + entry["user"]["discriminator"], "id": entry["id"]})
					output.log("Backed up friend " + entry["user"]["username"] + "#" + entry["user"]["discriminator"])
				case 2:
					data["blocked_users"].append({"username": entry["user"]["username"] + "#" + entry["user"]["discriminator"], "id": entry["id"]})
					output.log("Backed up blocked user " + entry["user"]["username"] + "#" + entry["user"]["discriminator"])
				case 3:
					data["outgoing_requests"].append({"username": entry["user"]["username"] + "#" + entry["user"]["discriminator"], "id": entry["id"]})
					output.log("Backed up outgoing request " + entry["user"]["username"] + "#" + entry["user"]["discriminator"])
				case 4:
					data["incoming_requests"].append({"username": entry["user"]["username"] + "#" + entry["user"]["discriminator"], "id": entry["id"]})
					output.log("Backed up incoming request " + entry["user"]["username"] + "#" + entry["user"]["discriminator"])
				case _:
					output.log("Unknown relationship type " + entry["type"])

		guilds = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
		guilds_data = guilds.json()

		for entry in guilds_data:

			guild = discord.utils.get(self.bot.guilds, id=int(entry["id"]))
			guild_invite = None
			for channel in guild.text_channels:
				if guild_invite == None:
					try:
						guild_invite = discum_client.createInvite(str(channel.id), 0, 0).json()['code']
					except:
						pass
			data["guilds"].append({"name": entry["name"], "id": entry["id"], "invite": guild_invite})
			output.log("Backed up guild " + entry["name"])

		with open(os.path.expanduser(f"{global_vars.user_info['config_path']}/backups/" + name + "/backup.json"), "w") as f:
			f.write(json.dumps(data, indent=4))
			output.log("Saved the backup to " + os.path.expanduser(f"{global_vars.user_info['config_path']}/backups/" + name + "/backup.json"))
	

	@commands.command(name="updaterpc", description="Updates the rpc", usage="updaterpc")
	async def updaterpc(self, ctx):
		settings = config.read()['rich_presence']
		discord_rpc.update_presence(**{
			'details': settings['details'],
			'state': settings['state'],
			'start_timestamp': time.time(),
			'large_image_key': settings['large_image'],
			'large_image_text': settings['large_text'],
			'small_image_key': settings['small_image'],
			'small_image_text': settings['small_text'],
		})



def setup(bot):
	bot.add_cog(Misc(bot))
