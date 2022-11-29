import os, sys

class global_vars:
	"""Contains global variables."""

	log_level = 0

	match(sys.platform):

		case "linux" | "linux2" | "darwin":
			user_info = {
				"home_path": str(os.path.expanduser('~')),
				"config_path": str(os.path.expanduser('~/.config/Vissarion')),
				"config_file": str(os.path.expanduser('~/.config/Vissarion/config.json'))
			}

		case "win32":
			user_info = {
				"home_path": str(os.path.expanduser('~\Documents')),
				"config_path": str(os.path.expanduser('~\Documents\Vissarion')),
				"config_file": str(os.path.expanduser('~\Documents\Vissarion\config.json'))
			}

	def _log(string: str):
		if(global_vars.log_level == 1):
			print(f"[DEBUG]:  {string}")
