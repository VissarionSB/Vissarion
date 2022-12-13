import asyncio, discum
from discord.ext import commands

from src.session import client
from src.console.output import output



class Raiding(commands.Cog):
	"""Contains 'malicious' commands related towards raiding."""

	def __init__(self, bot):
		self.bot = bot

	#automod's default mention limit is 20 and most of the servers are apparently too lazy to change it
	@commands.command(name="massping", aliases=["massmention"], description="Masspings the whole server", usage="massping <amount> (delay) (delete_after) (use_bypass) (bypass_limit)")
	async def massping(self, ctx, amount: int=1, delay: int=0, delete_after: int=0, bypass: bool=False, bypass_limit: int=19):
		

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

		members = get_members(str(ctx.guild.id), str(ctx.channel.id))
		output.log(f"Successfully fetched {len(members)} members")

		messages = []
		message = ""

		for member in members:
			if len(message) < 1950:
				if bypass == True and message.count("@") > bypass_limit:
					messages.append(message)
					message = ""
				message += f"<@{member}> "
			else:
				messages.append(message)
				message = ""

		messages.append(message)

		for _ in range(amount):
			for message in messages:
				try:
					await ctx.send(message, delete_after = delete_after)
					await asyncio.sleep(delay)
				except Exception as e:
					print(e)
					pass
				

				
def setup(bot):
	bot.add_cog(Raiding(bot))
