import requests, asyncio
from datetime import datetime

from src.discord_utils import discord_utils
from src.config import config
from src.session import client
from src.console.output import output


class session_manager:
	"""Manages the devices whitelist and logs out the unauthorized sessions."""

	def get_sessions() -> dict:
		"""Gets all of your logged sessions"""

		x_super_properties = discord_utils.get_x_super_properties()

		headers = {
			'Authorization': client.token,
			'User-Agent': client.get_random_useragent(),
			'X-Super-Properties': x_super_properties
		}
		request = requests.get("https://discord.com/api/v9/auth/sessions", headers=headers)

		return request.json()


	def logout_sessions(id_hashes: list):
		"""Logs you out of all sessions except the whitelisted ones"""

		x_super_properties = discord_utils.get_x_super_properties()
		
		headers = {
			'Authorization': client.token,
			'User-Agent': client.get_random_useragent(),
			'X-Super-Properties': x_super_properties
		}

		payload = {
			"session_id_hashes": id_hashes,
			"password": config.read()['user']['password']
		}

		request = requests.post("https://discord.com/api/v9/auth/sessions/logout", headers=headers, json=payload)
		
		if request.status_code != 200 or request.status_code == 204:
			output.log_sessions("Successfully logged out all unauthorized sessions.")
		else: 
			output.error(f"Couldn't logout sessions. Check your password and x-super-properties | Status code: ", separated_text=str(request.status_code))


	async def check_sessions():
		"""Checks if there are any unauthorized sessions and logs them out"""

		if(config.read()['session_manager']['enabled']):
			while True:
				if (config.read()['user']['password'] == ""):
					output.error("You need to set your password in the config file to use the devices whitelist feature.")
					return

				id_hashes = []
				for session in session_manager.get_sessions()['user_sessions']:
					
					id_hash = session["id_hash"]
					client_info = session["client_info"]

					last_time_used = datetime.strptime(session["approx_last_used_time"], "%Y-%m-%dT%H:%M:%S.%f%z").strftime('%Y-%m-%d | %H:%M:%S')

					if client_info['platform'] not in config.read()['session_manager']['platforms'] or client_info['os'] not in config.read()['session_manager']['operating_systems'] or client_info['location'] not in config.read()['session_manager']['locations'] :
						output.log_sessions("Unauthorized session: " + client_info['platform'] + " | " + client_info['os'] + " | " + client_info['location'] + " | " + last_time_used + " | " + id_hash)
						id_hashes.append(id_hash)
						output.log_sessions("Logged out: " + id_hash)

				if(id_hashes):
					session_manager.logout_sessions(id_hashes)     
				await asyncio.sleep(5)
