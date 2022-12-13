import discord, hashlib, bcrypt
from discord.ext import commands

from src.commands.utils.message_builder import builder
from src.session import client



class Hashes(commands.Cog):
	"""Contains commands for hashing text with some basic algorithms from the hashlib library."""

	def __init__(self, bot):
		self.bot = bot


	@commands.command(name="sha1", aliases=["sha-1"], description="Hashes a string using SHA-1", usage="sha1 <string>")
	async def sha1(self, ctx, *, string: str):

		encrypted_string = hashlib.sha1(string.encode("utf-8")).hexdigest()
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)	


	@commands.command(name="sha224", aliases=["sha-224"], description="Hashes a string using SHA-224", usage="sha224 <string>")
	async def sha224(self, ctx, *, string: str):

		encrypted_string = hashlib.sha224(string.encode("utf-8")).hexdigest()
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)	


	@commands.command(name="sha256", aliases=["sha-256"], description="Hashes a string using SHA-256", usage="sha256 <string>")
	async def sha256(self, ctx, *, string: str):

		encrypted_string = hashlib.sha256(string.encode("utf-8")).hexdigest()
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)	


	@commands.command(name="sha384", aliases=["sha-384"], description="Hashes a string using SHA-384", usage="sha384 <string>")
	async def sha384(self, ctx, *, string: str):

		encrypted_string = hashlib.sha384(string.encode("utf-8")).hexdigest()
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)	


	@commands.command(name="sha512", aliases=["sha-512"], description="Hashes a string using SHA-512", usage="sha512 <string>")
	async def sha512(self, ctx, *, string: str):

		encrypted_string = hashlib.sha512(string.encode("utf-8")).hexdigest()
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)	


	@commands.command(name="sha3_224", aliases=["sha-3_224"], description="Hashes a string using SHA-3_224", usage="sha3_224 <string>")
	async def sha3_224(self, ctx, *, string: str):

		encrypted_string = hashlib.sha3_224(string.encode("utf-8")).hexdigest()
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)	


	@commands.command(name="sha3_256", aliases=["sha-3_256"], description="Hashes a string using SHA-3_256", usage="sha3_256 <string>")
	async def sha3_256(self, ctx, *, string: str):

		encrypted_string = hashlib.sha3_256(string.encode("utf-8")).hexdigest()

		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)	


	@commands.command(name="sha3_384", aliases=["sha-3_384"], description="Hashes a string using SHA-3_384", usage="sha3_384 <string>")
	async def sha3_384(self, ctx, *, string: str):

		encrypted_string = hashlib.sha3_384(string.encode("utf-8")).hexdigest()

		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)


	@commands.command(name="sha3_512", aliases=["sha-3_512"], description="Hashes a string using SHA-3_512", usage="sha3_512 <string>")
	async def sha3_512(self, ctx, *, string: str):

		encrypted_string = hashlib.sha3_512(string.encode("utf-8")).hexdigest()

		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)

	
	@commands.command(name="blake2b", aliases=["blake-2b"], description="Hashes a string using Blake2b", usage="blake2b <string>")
	async def blake2b(self, ctx, *, string: str):

		encrypted_string = hashlib.blake2b(string.encode("utf-8")).hexdigest()

		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)


	@commands.command(name="blake2s", aliases=["blake-2s"], description="Hashes a string using Blake2s", usage="blake2s <string>")
	async def blake2s(self, ctx, *, string: str):

		encrypted_string = hashlib.blake2s(string.encode("utf-8")).hexdigest()
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)
	
	
	@commands.command(name="shake_128", aliases=["shake-128"], description="Hashes a string using SHAKE-128", usage="shake_128 [hexdigest] <string>")
	async def shake_128(self, ctx, hexdigest_value: int = 0, *, string: str):

		encrypted_string = hashlib.shake_128(string.encode("utf-8")).hexdigest(hexdigest_value)
		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)
	
	
	@commands.command(name="shake_256", aliases=["shake-256"], description="Hashes a string using SHAKE-256", usage="shake_256 [hexdigest] <string>")
	async def shake_256(self, ctx, hexdigest_value: int = 0, *, string: str):

		encrypted_string = hashlib.shake_256(string.encode("utf-8")).hexdigest(hexdigest_value)

		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)
	

	@commands.command(name="bcrypthash", aliases=["bcrypt-hash"], description="Hashes a string using Bcrypt", usage="bcrypthash <string>")
	async def bcrypthash(self, ctx, *, string: str):

		encoded_string = string.encode("utf-8")
		encrypted_string = bcrypt.hashpw(encoded_string, bcrypt.gensalt()).decode()

		message = f"""
		<field>
			Encrypted string
			<content>
				{encrypted_string}
			</content>
		</field>
		"""

		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)


	@commands.command(name="bcryptcheck", aliases=["bcrypt-check"], description="Validates a Bcrypt hash with a suggested string", usage="bcryptcheck <suggested_string> <hash>")
	async def bcryptcheck(self, ctx, first_hash: str, second_hash: str):

		first_string = first_hash.encode("utf-8")
		second_string = second_hash.encode("utf-8")
		result = bcrypt.checkpw(first_string, second_string)

		match(result):
			case True:
				result_msg = "The hashes match"
			case False:
				result_msg = "The hashes do not match"

		message = f"""
		<field>
			Result: 
			<content>
				{result_msg}
			</content>
		</field>
		"""
		await ctx.send(builder.message(str(ctx.command.name), message), delete_after=client.delete_after)
	

	
def setup(bot):
	bot.add_cog(Hashes(bot))
