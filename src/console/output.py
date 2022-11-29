import os, sys
from datetime import datetime

from src.console.ui import ui

class output:
	"""Contains functions that are used to output text to the console"""

	reset = "\x1b[39m"

	def clear():
		"""Clears the console"""
		
		match(sys.platform):
			case "linux" | "linux2" | "darwin":
				os.system("clear")
			case "win32":
				os.system("cls")	


	def get_time():
		"""Returns the current time."""
		return datetime.now().strftime("%H:%M")


	def cmd(string: str):
		"""Prints which command has been used at the time to the console."""
		print(f"[{ui.convert('$')}] | {ui.convert(output.get_time())} | Command used: {ui.convert(string)}")


	def log(string: str):
		"""Prints a log to the console."""
		print(f"[{ui.convert('$')}] | {ui.convert(output.get_time())} | {string}")


	def log_event(string: str):

		"""Prints an event to the console."""
		print(f"[{ui.convert('>')}] | {ui.convert(output.get_time())} | {ui.convert('EVENT')} | {string}")

	
	def log_sessions(string: str):

		"""Prints an event to the console."""
		print(f"[{ui.convert('>')}] | {ui.convert(output.get_time())} | {ui.convert('SESSIONS')} | {string}")


	def c_input(string: str):
		"""Gets input from the console."""
		c = input(f"[{ui.convert('/')}] | {ui.convert(output.get_time())} | {string}")
		return c


	def error(string: str, separated_text: str = None):
		"""Prints an error to the console."""
		print(f"[{ui.convert('!')}] | {ui.convert(output.get_time())} | {string} {ui.convert(separated_text) if separated_text else ''}")


	def print_banner(status: str, username: str, prefix: str):
		"""Prints the banner to the console with some basic information about the bot's configuration."""

		banner = '''
██╗   ██╗██╗███████╗███████╗ █████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
██║   ██║██║██╔════╝██╔════╝██╔══██╗██╔══██╗██║██╔═══██╗████╗  ██║
██║   ██║██║███████╗███████╗███████║██████╔╝██║██║   ██║██╔██╗ ██║
╚██╗ ██╔╝██║╚════██║╚════██║██╔══██║██╔══██╗██║██║   ██║██║╚██╗██║
 ╚████╔╝ ██║███████║███████║██║  ██║██║  ██║██║╚██████╔╝██║ ╚████║
  ╚═══╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝'''
		
		col = ui.get(banner.splitlines())
		columns = os.get_terminal_size().columns

		c_iter = 0
		for c in banner.splitlines():
			print(col[c_iter] + c.center(columns))
			c_iter += 1


		print(ui.shade(("─" * int(columns / 2.0)).center(columns)))

		print(f"{ui.convert('Status		<~ ')}{status}")
		print(f"{ui.convert('Account 	<~ ')}{username}")
		print(f"{ui.convert('Prefix		<~ ')}{prefix}")
		print()


	def refresh(username: str, prefix: str):
		"""Refreshes the console."""
		output.clear()
		output.print_banner("Connected", username, prefix)