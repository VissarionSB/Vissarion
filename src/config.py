import json, os
from src.globals import global_vars
from src.types.config_image import config_image

class config:
	"""Contains functions to validate and generate the config file as well as read and save it."""

	__config_image__ = config_image.default


	def _trash_collection():
		"""Used to remove unnecessary definitions from the config file."""

		__current_config__ = config.read()

		for key in list(__current_config__.keys()):
			if key not in config.__config_image__.keys():
				__current_config__.pop(key)

			if type(key) == dict:
				for subkey in list(key.keys()):
					if subkey not in config.__config_image__[key].keys():
						__current_config__[key].pop(subkey)

		config.save(__current_config__)


	def _check_types():
		"""Used to check if the config file has the correct types."""

		__current_config__ = config.read()

		for key in list(__current_config__.keys()):
			if type(__current_config__[key]) != type(config.__config_image__[key]):
				__current_config__[key] = config.__config_image__[key]

			if type(__current_config__[key]) == dict:
				for subkey in list(__current_config__[key].keys()):
					if type(__current_config__[key][subkey]) != type(config.__config_image__[key][subkey]):
						__current_config__[key][subkey] = config.__config_image__[key][subkey]

		config.save(__current_config__)


	def _check_restricted_values():
		"""Used to check if the restricted keys have the correct values."""

		__current_config__ = config.read()

		for key, value in list(__current_config__.items()):
			if key in config_image.restricted_values:
				if type(config_image.restricted_values[key]) == dict:
					for subkey in list(config_image.restricted_values[key].keys()):
						if value[subkey] not in config_image.restricted_values[key][subkey]:
							__current_config__[key][subkey] = config_image.restricted_values[key][subkey][0]
						
		config.save(__current_config__)


	def _refresh_keys():
		"""Used to find missing keys and add them back to the config file."""

		__current_config__ = config.read()

		__current_config_keys__ = list(__current_config__.keys())
		__default_config_keys__ = list(config.__config_image__.keys())

		for key in list(__default_config_keys__):
			if key not in __current_config_keys__:
				__current_config__[key] = config.__config_image__[key]

			if type(key) == dict:
				for subkey in list(key.keys()):
					if subkey not in __current_config__[key].keys():
						__current_config__[key][subkey] = config.__config_image__[key][subkey]

		config.save(__current_config__)
		
		
	def _revert():
		"""Used to revert the config file to the default values."""
		config.save(config_image.default)


	def _check():
		"""Used to check if the config file is valid using all of the four functions above."""
		
		try:
			config._trash_collection()
			config._refresh_keys()
			config._check_restricted_values()
			config._check_types()
		except json.decoder.JSONDecodeError:
			config._revert()


	def init():
		"""Used to initialize and generate the config file."""

		if not os.path.exists(global_vars.user_info["config_path"]): 
			os.makedirs(global_vars.user_info["config_path"])

		if not os.path.isfile(global_vars.user_info["config_file"]): 

			with open(global_vars.user_info["config_file"], "w") as f:
				json.dump(config_image.default, f, indent=4, sort_keys=False)
				f.close()
		
		config._check()


	def read() -> dict:
		"""Used to read the config file and return it as a dictionary."""
		return json.load(open(global_vars.user_info["config_file"]))


	def save(data: dict):
		"""Used to save multiple entries in the config file."""
		return json.dump(data, open(global_vars.user_info["config_file"], "w"), indent=4, sort_keys=False)


	def save_key(key: str, value: str, subkey: str = None, ):
		"""Used to save just one entry in the config file."""

		if (subkey):
			__current_config__ = config.read()
			__current_config__[key][subkey] = value
			config.save(__current_config__)
		else:
			__current_config__ = config.read()
			__current_config__[key] = value
			config.save(__current_config__)

	
	def read_key(key: str, subkey: str = None):
		"""Used to read just one entry in the config file."""

		if (subkey):
			__current_config__ = config.read()
			return __current_config__[key][subkey]
		else:
			__current_config__ = config.read()
			return __current_config__[key]

	
