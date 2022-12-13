import discord, asyncio, os, requests
from discord.ext import commands
from datetime import datetime

from src.console.output import output
from src.config import config
from src.commands.utils.webhook_builder import webhook_builder



class Events(commands.Cog):
	"""Logs events from all over da discord"""

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_message_delete(self, message):
		if(config.read()['event_logger']['enabled'] == True and config.read()['event_logger']['message_delete'] == True):
			output.log_event(f"Message deleted in {message.channel.name} by {message.author.name}#{message.author.discriminator} ({message.author.id}) | {message.guild}")
			output.log_event(f"Message content: {message.content}")
			webhook_data = webhook_builder.form_webhook_data("Message Deleted", 
			{	"Guild": message.guild, 
				"Channel": message.channel.name, 
				"Author": f"{message.author.name}#{message.author.discriminator} ({message.author.id})", 
				"Message": message.content
			})
			r = requests.post(config.read()['webhook_urls']['message_delete_url'], json=webhook_data)
			if "401: Unauthorized" in str(r.content):
				output.error("Invalid webhook provided for the message_delete event")
	
	
	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		if(config.read()['event_logger']['enabled'] == True and config.read()['event_logger']['message_edit'] == True):
			output.log_event(f"Message edited in {before.channel.name} by {before.author.name}#{before.author.discriminator} ({before.author.id}) | {before.guild}")
			output.log_event(f"Before: {before.content}")
			output.log_event(f"After: {after.content}")
			webhook_data = webhook_builder.form_webhook_data("Message Edited", 
			{	"Guild": before.guild, 
				"Channel": before.channel.name, 
				"Author": f"{before.author.name}#{before.author.discriminator} ({before.author.id})", 
				"Before": before.content,
				"After": after.content
			})
			r = requests.post(config.read()['webhook_urls']['message_edit_url'], json=webhook_data)
			if "401: Unauthorized" in str(r.content):
				output.error("Invalid webhook provided for the message_delete event")


	@commands.Cog.listener()
	async def on_member_join(self, member):
		if(config.read()['event_logger']['enabled'] == True and config.read()['event_logger']['member_join'] == True):
			output.log_event(f"{member.name}#{member.discriminator} ({member.id}) joined {member.guild}")
			webhook_data = webhook_builder.form_webhook_data("Member Joined", 
			{	"Guild": member.guild, 
				"Member": f"{member.name}#{member.discriminator} ({member.id})"
			})
			r = requests.post(config.read()['webhook_urls']['member_join_url'], json=webhook_data)
			if "401: Unauthorized" in str(r.content):
				output.error("Invalid webhook provided for the member_join event")
	

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		if(config.read()['event_logger']['enabled'] == True and config.read()['event_logger']['member_leave'] == True):
			if member == self.bot.user:
				output.log_event(f"You left {member.guild} (You might've been kicked)")
				webhook_data = webhook_builder.form_webhook_data("Member Left", 
				{	"Guild": member.guild, 
					"Member": f"You"
				})
				r = requests.post(config.read()['webhook_urls']['member_leave_url'], json=webhook_data)
				if "401: Unauthorized" in str(r.content):
					output.error("Invalid webhook provided for the member_leave event")

			else:
				output.log_event(f"{member.name}#{member.discriminator} ({member.id}) left {member.guild}")
				webhook_data = webhook_builder.form_webhook_data("Member Left", 
				{	"Guild": member.guild, 
					"Member": f"{member.name}#{member.discriminator} ({member.id})"
				})
				r = requests.post(config.read()['webhook_urls']['member_leave_url'], json=webhook_data)
				if "401: Unauthorized" in str(r.content):
					output.error("Invalid webhook provided for the member_leave event")
	

	@commands.Cog.listener()
	async def on_member_ban(self, guild, user):
		if(config.read()['event_logger']['enabled'] == True and config.read()['event_logger']['member_ban'] == True):
			if user == self.bot.user:
				output.log_event(f"You were banned from {guild}")
				webhook_data = webhook_builder.form_webhook_data("Member Banned", 
				{	"Guild": guild, 
					"Member": f"You"
				})
				r = requests.post(config.read()['webhook_urls']['member_ban_url'], json=webhook_data)
				if "401: Unauthorized" in str(r.content):
					output.error("Invalid webhook provided for the member_ban event")
		
			else:
				output.log_event(f"{user.name}#{user.discriminator} ({user.id}) was banned from {guild}")
				webhook_data = webhook_builder.form_webhook_data("Member Banned", 
				{	"Guild": guild, 
					"Member": f"{user.name}#{user.discriminator} ({user.id})"
				})
				r = requests.post(config.read()['webhook_urls']['member_ban_url'], json=webhook_data)
				if "401: Unauthorized" in str(r.content):
					output.error("Invalid webhook provided for the member_ban event")

	
	@commands.Cog.listener()
	async def on_typing(self, channel, user, when):
		if(config.read()['event_logger']['enabled'] == True and config.read()['event_logger']['dm_typing'] == True):
			if channel.type == discord.ChannelType.private:
				output.log_event(f"{user.name}#{user.discriminator} ({user.id}) is typing in your DMs")
				
	

def setup(bot):
	bot.add_cog(Events(bot))
