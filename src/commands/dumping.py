import discord, asyncio, os, discum
from discord.ext import commands
from datetime import datetime

from src.session import client
from src.console.output import output
from src.globals import global_vars



class Dumping(commands.Cog):
	"""Contains commands that are used to dump stuff."""

	def __init__(self, bot):
		self.bot = bot
		
		
	def _dir_guild_check(guild_id: str):
		if not os.path.exists(f"{global_vars.user_info['config_path']}/dumps/" + guild_id):
			os.makedirs(f"{global_vars.user_info['config_path']}/dumps/" + guild_id)


	def _dir_channel_check(guild_id: str, channel_id: str):
		if not os.path.exists(f"{global_vars.user_info['config_path']}/dumps/" + guild_id + "/" + channel_id):
			os.makedirs(f"{global_vars.user_info['config_path']}/dumps/" + guild_id + "/" + channel_id)


	@commands.command(name="dumpmessages", aliases=["dumpmsgs", "dmsgs"], description="Dumps messages from a channel", usage="dumpmessages (channel_id) (limit)")
	async def dumpmessages(self, ctx, channel_id: str=None, limit:int=1000):
		
		if (channel_id == None):
			channel = ctx.channel

		else:
			channel = self.bot.get_channel(int(channel_id))
		
		output.log("Dumping messages from channel " + str(channel.id))

		Dumping._dir_guild_check(str(ctx.guild.id))
		Dumping._dir_channel_check(str(ctx.guild.id), str(channel.id))

		content = ""

		async for message in channel.history(limit=limit):
			content += f"{message.created_at.strftime('%m/%d/%Y | %H:%M:%S')} <~ {message.author.name}#{message.author.discriminator}: {message.content}\n"
			
		open(f"{global_vars.user_info['config_path']}/dumps/" + str(ctx.guild.id) + "/" + str(channel.id) + "/messages.txt", "w").write(content)
		output.log("Dumped messages from channel " + str(channel.id))


	@commands.command(name="dumpchannels", aliases=["dchannels", "dchans"], description="Dumps channels from a guild", usage="dumpchannels (guild_id)")
	async def dumpchannels(self, ctx, guild_id: str=None):

		if (guild_id == None):
			guild = ctx.guild

		else:
			guild = self.bot.get_guild(int(guild_id))

		output.log("Dumping channels from guild " + str(guild.id))
		Dumping._dir_guild_check(str(ctx.guild.id))

		content = ""

		for channel in guild.channels:
			content += f"{channel.name} ({channel.id})\n"

		open("{global_vars.user_info['config_path']}/dumps/" + str(guild.id) + "/channels.txt", "w").write(content)
		output.log("Dumped channels from guild " + str(guild.id))


	@commands.command(name="dumpmembers", aliases=["dmembers", "dmems"], description="Dumps members from a guild", usage="dumpmembers (guild_id)")
	async def dumpmembers(self, ctx, guild_id: str=None, channel_id: str=None):
	
		Dumping._dir_guild_check(str(ctx.guild.id))

		if (guild_id == None):
			guild = ctx.guild

		else:
			guild = self.bot.get_guild(int(guild_id))

		if(channel_id == None):
			channel = ctx.channel

		else:
			channel = self.bot.get_guild(int(channel_id))

		output.log("Dumping members from guild " + str(guild.id))
		
		discum_client = discum.Client(token=client.token, log=False, user_agent=client.get_random_useragent())

		def close_after_fetching(resp, guild_id):          
			if discum_client.gateway.finishedMemberFetching(guild_id):
				members = discum_client.gateway.session.guild(guild_id).members
				discum_client.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
				discum_client.gateway.close()
				return members

		def get_members(guild_id, channel_id):
			discum_client.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
			discum_client.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
			discum_client.gateway.run()
			discum_client.gateway.resetSession()
			return discum_client.gateway.session.guild(guild_id).members

		members = get_members(str(guild.id), str(channel.id))
		content = ""

		for key in members.keys():
			try:
				username = f"{members[key]['username']}#{members[key]['discriminator']}"
				id = members[key]['presence']['user']['id']
				joined_at = datetime.strptime(members[key]["joined_at"], "%Y-%m-%dT%H:%M:%S.%f%z").strftime('%Y-%m-%d | %H:%M:%S')
				content += f"{username} 			({id}) | 			joined at: {joined_at}\n"
				
			except:
				pass

		open(f"{global_vars.user_info['config_path']}/dumps/" + str(guild.id) + "/members.txt", "w").write(content)
		output.log("Dumped members from guild " + str(guild.id))



def setup(bot):
	bot.add_cog(Dumping(bot))
