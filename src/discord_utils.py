import requests, re, random, base64, ua_parser.user_agent_parser
from src.session import client
from src.config import config

class discord_utils:

	#https://github.com/Merubokkusu/Discord-S.C.U.M/blob/a814f9500429ebd6b31c93cbae3c330bd8f1f89a/discum/start/superproperties.py


	def get_build_number() -> str:
		"""Gets the build number of the current discord client"""
		
		headers = {
			"Sec-Fetch-Dest": "document", 
			"Sec-Fetch-Mode": "navigate",
			"Sec-Fetch-Site": "none"
		}

		try:
			login_page_req = requests.get("https://discord.com/login", headers=headers)
			file_with_build_number = 'https://discord.com/assets/' + re.compile(r'assets/+([a-z0-9]+)\.js').findall(login_page_req.text)[-2] + '.js'

			build_num_req = requests.get(file_with_build_number, headers=headers)
			index_of_build_num = build_num_req.text.find('buildNumber') + 24
			build_num = str(build_num_req.text[index_of_build_num:index_of_build_num + 6])

		except: 
			build_num = "97507"

		return build_num


	def get_x_super_properties() -> str:
		"""Generates x-super-properties for anti-bot detection"""

		if config.read()['useOwnXProperties']['enabled']:
			x_super_properties = config.read()['useOwnXProperties']['x-property']
			
		else:
			
			user_agent = client.get_random_useragent()
			parsed_useragent = ua_parser.user_agent_parser.Parse(user_agent)

			browser_ver_list = [parsed_useragent["user_agent"]["major"], parsed_useragent["user_agent"]["minor"], parsed_useragent["user_agent"]["patch"]]
			os_ver_list = [parsed_useragent["os"]["major"], parsed_useragent["os"]["minor"], parsed_useragent["os"]["patch"]]

			template = {
				"os": parsed_useragent["os"]["family"],
				"browser": parsed_useragent["user_agent"]["family"],
				"device": "",
				"system_locale": "en-US",
				"browser_user_agent": parsed_useragent["string"],
				"browser_version": ".".join(filter(None, browser_ver_list)),
				"os_version": ".".join(filter(None, os_ver_list)),
				"referrer": "",
				"referring_domain": "",
				"referrer_current": "",
				"referring_domain_current": "",
				"release_channel": "stable",
				"client_build_number": int(discord_utils.get_build_number()),
				"client_event_source": None
			}

			super_property = base64.b64encode(str(template).encode('utf-8')).decode()
			return super_property


	def get_spotify_access_token() -> str:
		"""Gets the spotify api key for the current discord client"""

		headers = {
			"Authorization": client.token,
			"Sec-Fetch-Dest": "document", 
			"Sec-Fetch-Mode": "navigate",
			"Sec-Fetch-Site": "none"
		}

		req = requests.get("https://discord.com/api/v9/users/@me/connections", headers=headers)
		data = req.json()

		for connection in data:
			if connection["type"] == "spotify":
				return connection["access_token"]
				
		return None