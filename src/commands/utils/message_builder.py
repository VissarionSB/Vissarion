from src.config import config
from src.commands.utils.parser import parser

class builder:


	def _embed(author: str, content: str):

		host = 			config.read()['embeds']['host']
		title =			config.read()["embeds"]["title"]
		color =			config.read()["embeds"]["color"]
		image_url =		config.read()["embeds"]["image_url"]
		large =			config.read()["embeds"]["large"]
		footer =		config.read()["embeds"]["footer"]

		content = content + f"<nl> {footer}"
		content = parser.parse_embed(content)

		if host == "vaul.xyz":
			api_url = ("https://embeds.vaul.xyz/api/?author=%s&title=%s&description=%s&color=%s&image_url=%s&large=%s" % (author, title, content, color.replace("#", ""), image_url, str(large).lower()))
			spoiled_url = f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| {api_url}"
			return spoiled_url 
	

	def _ansi(author: str, content: str):

		title = 	config.read()["ansi"]["title"]
		footer = 	config.read()["ansi"]["footer"]

		base = f"""
<quote>**{title}**<nl>
<quote><nl>
<quote><nl>
<quote>```ansi<nl>
<quote><bold>{title}<reset> » <col_purple>{author}<reset><nl>
<quote>```<nl>
<quote>```ansi<nl>
{content}
<quote>```<nl>
<quote><nl>
<quote>{footer}<nl>
		"""
		
		message = parser.parse_ansi(base)
		return message


	def message(command_name: str, content: str):

		match(config.read()["commands"]["command_mode"]):
	
			case "embed":
				return builder._embed(command_name, content)
		
			case "ansi":
				return builder._ansi(command_name, content)
