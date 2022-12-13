import discord, asyncio, requests
from discord.ext import commands

from src.session import client
from src.config import config
from src.console.output import output
from src.commands.utils.message_builder import builder



class Networking(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ipinfo", aliases=["ip", "iplookup"], description="Gets information about an IP address", usage="ipinfo <ip>")
	async def ipinfo(self, ctx, ip: str):

		headers = {
			"Authorization": client.token,
			"Content-Type": "application/json"
		}

		response = requests.get("http://ip-api.com/json/" + ip, headers=headers)

		if response.status_code == 200 and response.json()["status"] == "success":
	
			data = response.json()
			message = f"""
<field>
	<bold>IP<reset>
	<content>
		{data['query']}
	</content>
</field>
<quote><nl>
<field>
	Country
	<content>
		{data['country']}
	</content>
</field>
<field>
	Country Code
	<content>
	  	{data['countryCode']}
	</content>
</field>
<field>
	Region
	<content>
		{data['regionName']}
	</content>
</field>
<field>
	City
	<content>
		{data['city']}
	</content>
</field>
<field>
	ISP
	<content>   
		{data['isp']}
	</content>
</field>
<field>
	Timezone
	<content>
		{data['timezone']}
	</content>
</field>
<field>
	Lat/Long
	<content> 
	{data['lat']}, {data['lon']}
	</content>
</field>
<field>
	AS
	<content>
		{data['as']}
	</content>
</field>
<field>
	AS Organization
	<content>
		{data['org']}
	</content>
</field>
<field>
Zip Code
	<content>
		{data['zip']}
	</content>
</field>    """
			await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)

		else:
			output.error("Invalid IP address")

	@commands.command(name="zonetransfer", aliases=["zonetrans", "dnszonetransfer", "dnszonetrans"], description="Checks if a domain is vulnerable to a DNS zone transfer", usage="zonetransfer <domain>")
	async def zonetransfer(self, ctx, domain: str):

		r = requests.get(f'https://api.hackertarget.com/zonetransfer/?q={domain}')

		if r.status_code == 200:
			await ctx.send(builder.message(str(ctx.command.name), "<text><bold>Output logs will be shown below<reset></text>"), delete_after=client.delete_after)
			await ctx.send(f"```{r.text}```", delete_after=client.delete_after)

		else:
			output.error("Invalid domain")
	

	@commands.command(name="dnslookup", aliases=["dns"], description="Gets information about a domain", usage="dnslookup <domain>")
	async def dnslookup(self, ctx, domain: str):
		
		r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={domain}')

		if r.status_code == 200:
			await ctx.send(builder.message(str(ctx.command.name), "<text><bold>Output logs will be shown below<reset></text>"), delete_after=client.delete_after)
			await ctx.send(f"```{r.text}```", delete_after=client.delete_after)

		else:
			output.error("Invalid domain")


	@commands.command(name="httpheaders", aliases=["httpheader", "headers", "header"], description="Gets HTTP headers of a website", usage="httpheaders <domain>")
	async def httpheaders(self, ctx, domain: str):

		r = requests.get(f'https://api.hackertarget.com/httpheaders/?q={domain}')

		if r.status_code == 200:
			await ctx.send(builder.message(str(ctx.command.name), "<text><bold>Output logs will be shown below<reset></text>"), delete_after=client.delete_after)
			await ctx.send(f"```{r.text}```", delete_after=client.delete_after)
		
		else:
			output.error("Invalid domain")

	
	@commands.command(name="asn", aliases=["aslookup"], description="Gets information about an ASN", usage="asn <asn>")
	async def asn(self, ctx, asn: str):

		r = requests.get(f'https://api.hackertarget.com/aslookup/?q={asn}')

		if r.status_code == 200:
			await ctx.send(builder.message(str(ctx.command.name), "<text><bold>Output logs will be shown below<reset></text>"), delete_after=client.delete_after)
			await ctx.send(f"```{r.text}```", delete_after=client.delete_after)

		else:
			output.error("Invalid ASN")
	

	@commands.command(name="reverseip", aliases=["reverse", "reverseiplookup"], description="Gets information about an IP address", usage="reverseip <ip>")
	async def reverseip(self, ctx, ip: str):

		r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')

		if r.status_code == 200:
			await ctx.send(builder.message(str(ctx.command.name), "<text><bold>Output logs will be shown below<reset></text>"), delete_after=client.delete_after)
			await ctx.send(f"```{r.text}```", delete_after=client.delete_after)

		else:
			output.error("Invalid IP address")
	

	@commands.command(name="crawl", aliases=["crawler", "webcrawler", "webcrawl"], description="Crawls a website", usage="crawl <domain>")
	async def crawl(self, ctx, domain: str):

		r = requests.get(f'https://api.hackertarget.com/pagelinks/?q={domain}')

		if r.status_code == 200:
			await ctx.send(builder.message(str(ctx.command.name), "<text><bold>Output logs will be shown below<reset></text>"), delete_after=client.delete_after)
			await ctx.send(f"```{r.text}```", delete_after=client.delete_after)

		else:
			output.error("Invalid domain")
		
	
	@commands.command(name="subdomain", aliases=["subdomains", "subdomainfinder"], description="Finds subdomains of a domain", usage="subdomain <domain>")
	async def subdomain(self, ctx, domain: str):
		
		r = requests.get(f'https://api.hackertarget.com/hostsearch/?q={domain}')

		if r.status_code == 200:
			await ctx.send(builder.message(str(ctx.command.name), "<text><bold>Output logs will be shown below<reset></text>"), delete_after=client.delete_after)
			await ctx.send(f"```{r.text}```", delete_after=client.delete_after)
		
		else:
			output.error("Invalid domain")






def setup(bot):
	bot.add_cog(Networking(bot))
