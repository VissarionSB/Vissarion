class parser:

	ansi_syntax = {
		"<col_gray>": 		"[30m",
		"<col_red>":		"[31m",
		"<col_green>": 		"[32m",
		"<col_yellow>":		"[33m",
		"<col_blue>":		"[34m",
		"<col_purple>":		"[35m",
		"<col_cyan>":		"[36m",
		"<col_white>":		"[37m",
		"<reset>":		"[0m",
		"<bold>": 		"[1m",
		"<nl>": 		"\n",
		"<tl>": 		"\t",
		"<quote>": 		"> "
	}


	ansi_syntax_sets = {
		"<field>":	"<quote>",
		"</field>":		"<reset><nl>",
		"<content>":	"<nl><quote><tl><col_gray>",
		"</content>":	"<reset>",
		"<text>":		"<quote>",
		"</text>":		"<nl>",
	}


	embed_syntax = { #lol
		"<col_gray>": 		"",
		"<col_red>":		"",
		"<col_green>": 		"",
		"<col_yellow>":		"",
		"<col_blue>":		"",
		"<col_purple>":		"",
		"<col_cyan>":		"",
		"<col_white>":		"",
		"<reset>":		"",
		"<bold>": 		"",
		"<nl>": 		"%0A",
		"<tl>": 		"%20",
		"<quote>": 		"",
		" ": 			"%20",
	}


	embed_syntax_sets = { #lol
		"<field>":	"",
		"</field>":		"%0A",
		"<content>":	":%20",
		"</content>":	"",
		"<text>":		"",
		"</text>":		"",
	}


	def _parse_ansi_syntax(content: str):
		for key, value in parser.ansi_syntax.items():
			content = content.replace(key, value)
		return content


	def _parse_ansi_syntax_sets(content: str):
		content = content.strip()

		for key, value in parser.ansi_syntax_sets.items():
			content = content.replace(key, value)

		return content.replace("\n", "").replace("\t", "")


	def _parse_ansi_syntax_all(content: str):
		content = parser._parse_ansi_syntax_sets(content)
		content = parser._parse_ansi_syntax(content)

		return content


	def _parse_embed_syntax(content: str):
		for key, value in parser.embed_syntax.items():
			content = content.replace(key, value)
		return content


	def _parse_embed_syntax_sets(content: str):
		content = content.strip()

		for key, value in parser.embed_syntax_sets.items():
			content = content.replace(key, value)
		return content.replace("\n", "").replace("\t", "")


	def _parse_embed_syntax_all(content: str):
		content = parser._parse_embed_syntax_sets(content)
		content = parser._parse_embed_syntax(content)

		return content


	def parse_ansi(content: str):
		content = parser._parse_ansi_syntax_all(content)
		return content


	def parse_embed(content: str):
		content = parser._parse_embed_syntax_all(content)
		return content