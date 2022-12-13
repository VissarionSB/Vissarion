import requests
from discord.ext import commands

from src.console.output import output
from src.discord_utils import discord_utils



class Spotify(commands.Cog):
	"""Contains commands that are used to control the spotify player"""

	def __init__(self, bot):
		self.bot = bot
		self.player_prefix = "https://api.spotify.com/v1/me/player/"
		self.shuffle_state = False


	def _get_headers(token: str):
		return { "Authorization": "Bearer " + token }


	@commands.command(name="unpause", aliases=["resume"], description="Unpauses the player", usage="unpause")
	async def unpause(self, ctx):

		spotify_token = discord_utils.get_spotify_access_token()

		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return

		r = requests.put(self.player_prefix + "play", headers=Spotify._get_headers(spotify_token))


	@commands.command(name="pause", aliases=[], description="Pauses the player", usage="pause")
	async def pause(self, ctx):

		spotify_token = discord_utils.get_spotify_access_token()

		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return

		r = requests.put(self.player_prefix + "pause", headers=Spotify._get_headers(spotify_token))


	@commands.command(name="next", aliases=[], description="Skips to the next song", usage="next")
	async def next(self, ctx):

		spotify_token = discord_utils.get_spotify_access_token()

		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return

		r = requests.post(self.player_prefix + "next", headers=Spotify._get_headers(spotify_token))


	@commands.command(name="previous", aliases=[], description="Skips back to the previous song", usage="previous")
	async def previous(self, ctx):

		spotify_token = discord_utils.get_spotify_access_token()

		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return

		r = requests.post(self.player_prefix + "previous", headers=Spotify._get_headers(spotify_token))


	@commands.command(name="shuffle", aliases=[], description="Toggles shuffle", usage="shuffle")
	async def shuffle(self, ctx):

		spotify_token = discord_utils.get_spotify_access_token()

		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return

		self.shuffle_state = not self.shuffle_state

		r = requests.put(self.player_prefix + "shuffle", headers=Spotify._get_headers(spotify_token), params={"state": self.shuffle_state})


	@commands.command(name="repeat", aliases=[], description="Toggles repeat", usage="repeat <state>")
	async def repeat(self, ctx, state: str):

		spotify_token = discord_utils.get_spotify_access_token()

		states = ["track", "context", "off"]

		if state in states:

			if spotify_token == None:
				output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
				return

			r = requests.put(self.player_prefix + "repeat", headers=Spotify._get_headers(spotify_token), params={"state": state})
		
		else:
			output.error("Invalid state. Valid states <~ ", separated_text="track, context, off")


	@commands.command(name="volume", aliases=[], description="Sets the volume", usage="volume <volume>")
	async def volume(self, ctx, volume: int):

		spotify_token = discord_utils.get_spotify_access_token()

		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return
		
		if volume < 0 or volume > 100:
			output.error("SPOTIFY <~ Volume must be between 0 and 100%")
			return

		r = requests.put(self.player_prefix + "volume", headers=Spotify._get_headers(spotify_token), params={"volume_percent": volume})
		

	@commands.command(name="seek", aliases=[], description="Seeks to a position in the current song (in seconds)", usage="seek <position>")
	async def seek(self, ctx, position: int):
		secs = position * 1000

		spotify_token = discord_utils.get_spotify_access_token()

		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return

		r = requests.put(self.player_prefix + "seek", headers=Spotify._get_headers(spotify_token), params={"position_ms": secs})


	@commands.command(name="play", aliases=[], description="Plays a song", usage="play <song>")
	async def play(self, ctx, *, song: str):

		spotify_token = discord_utils.get_spotify_access_token()


		if spotify_token == None:
			output.error("SPOTIFY <~ Invalid access token. Please check if your spotify account is linked to your discord account")
			return

		search = requests.get("https://api.spotify.com/v1/search", headers=Spotify._get_headers(spotify_token), params={"q": song, "type": "track"})
		search = search.json()


		if search["tracks"]["items"][0] == None:
			output.error("SPOTIFY <~ No songs found")
			return

		track = search["tracks"]["items"][0]
		name = track["name"]
		track_uri = track["uri"]

		queue_post = requests.post(self.player_prefix + "queue", headers=Spotify._get_headers(spotify_token), params={"uri": track_uri})

		if queue_post.status_code != 204:
			output.error("SPOTIFY <~ Failed to play the song")
			return

		r = requests.post(self.player_prefix + "next", headers=Spotify._get_headers(spotify_token))

		if r.status_code == 204:
			output.success(f"SPOTIFY <~ Playing {name}")
		else:
			output.error("SPOTIFY <~ Failed to play the song")
			return



def setup(bot):
	bot.add_cog(Spotify(bot))
