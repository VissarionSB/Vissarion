
import discord_rpc, time, requests, random
from discord.ext import commands
from threading import Thread

from src.config import config
from src.console.output import output


class client:
	"""Contains some basic client functionality and variables."""

	token = config.read()['user']['token']
	prefix = config.read()['commands']['prefix']
	delete_after = config.read()['commands']['delete_after']

	def _refresh_prefix():
		"""Refreshes the prefix variable."""
		client.prefix = config.read()['commands']['prefix']
		
	def _change_token_seq(bot: commands.Bot):
		"""Changes the token in the config file and restarts the bot."""
		p_token = output.c_input("Please enter your token: ").replace('"', '')

		chu = requests.get("https://discord.com/api/users/@me", headers={"Authorization": p_token})
		
		if chu.status_code == 200:
			config.save_key("user", p_token, subkey="token")
			client.token = p_token
			request = chu.json()
			username = request["username"]
			discriminator = request["discriminator"]
			output.clear()
			output.print_banner("Connecting...", f"{username}#{discriminator}", config.read()['commands']['prefix'])
			bot.run(p_token)
			
		else:
			output.log("Invalid token.")
			client._change_token_seq(bot)


	def _initialize_rpc_worker():
		"""Starts the Discord Rich Presence"""

		if (config.read()["rich_presence"]['enabled'] == True):
			try:

				settings = config.read()["rich_presence"]

				discord_rpc.initialize(settings['client_id'],	log=False)
				discord_rpc.update_presence(**{
					'details': settings['details'],
					'state': settings['state'],
					'start_timestamp': time.time(),
					'large_image_key': settings['large_image'],
					'large_image_text': settings['large_text'],
					'small_image_key': settings['small_image'],
					'small_image_text': settings['small_text'],
				})
				for _ in range(3):
					time.sleep(1)
					discord_rpc.update_connection()
					discord_rpc.run_callbacks()
				output.log("Initialized the rich presence")
			except:
				pass

	def start_rpc():
		""" Starts up the entire thing """

		rpc_thread = Thread(target=client._initialize_rpc_worker)
		rpc_thread.start()

	def connect(bot: commands.Bot):
		"""Connects the bot to Discord and validates your token."""

		output.clear()
		output.log("Loading...")

		if(client.token == "token-here" or ""):
			client._change_token_seq(bot)
			return

		usr_r = requests.get("https://discord.com/api/users/@me", headers={"Authorization": client.token})

		if usr_r.status_code == 200:
			request = usr_r.json()
			username = request["username"]
			discriminator = request["discriminator"]
			output.clear()
			output.print_banner("Connecting...", f"{username}#{discriminator}", config.read()['commands']['prefix'])

		else:
			output.log("Invalid token.")
			client._change_token_seq(bot)
			return

		try:
			bot.run(client.token)
		except Exception as err:
			print(err)


	def get_random_useragent() -> str:
		"""Gets a random useragent from the useragents list"""

		userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
		return random.choice(userAgents)		
