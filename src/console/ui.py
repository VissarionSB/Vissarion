from src.config import config

class ui:
	"""Contains functions to stylize the console output."""

	def hex_to_rgb(str: hex):

		str = str.lstrip('#')
		l = len(str)
		return tuple(int(str[i:i+l//3], 16) for i in range(0, l, l//3))


	def get_gradient_range(start_hex: str, end_hex: str, steps: int = 10):
		"""Interpolates your stuff and returns the values"""
	
		start = ui.hex_to_rgb(start_hex)
		end =   ui.hex_to_rgb(end_hex)

		rs, gs, bs = [start[0]], [start[1]], [start[2]]

		for t in range(1, steps):
			rs.append(start[0] + (t * (end[0] - start[0]) // steps))
			gs.append(start[1] + (t * (end[1] - start[1]) // steps))
			bs.append(start[2] + (t * (end[2] - start[2]) // steps))

		return list(zip(rs, gs, bs))


	def convert(string: str):
		"""Converts a string to a colorized string with gradient."""
	
		col_array = []
		base_iter = 0
		base_string = ""

		primary_col =   config.read()["console"]["primary_color"]
		secondary_col = config.read()["console"]["secondary_color"]

		colors = ui.get_gradient_range(primary_col, secondary_col, len(string))
	
		for color in colors:
			r, g, b = color[0], color[1], color[2]
			fg = f'\033[38;2;{r};{g};{b}m'
			col_array.append(fg)

		for character in string: 
			base_string += "" + col_array[base_iter] + character 
			base_iter += 1

		string = base_string + "\x1b[39m"
		return string


	def get(string: str):
		"""Returns the color array with 16 bit fg values."""
	
		col_array = []
		base_iter = 0
		base_string = ""

		primary_col =   config.read()["console"]["primary_color"]
		secondary_col = config.read()["console"]["secondary_color"]

		colors = ui.get_gradient_range(primary_col, secondary_col, len(string))
	
		for color in colors:
			r, g, b = color[0], color[1], color[2]
			fg = f'\033[38;2;{r};{g};{b}m'
			col_array.append(fg)

		return col_array


	def shade(string: str):
		"""Shades the text from sides to center."""

		col_array = []
		base_iter = 0
		base_string = ""

		primary_col =   config.read()["console"]["primary_color"]
		secondary_col = config.read()["console"]["secondary_color"]



		left_colors = ui.get_gradient_range(primary_col, secondary_col, len(string))
		right_colors = ui.get_gradient_range(secondary_col, primary_col, len(string))
	   
		for color in left_colors:
			r, g, b = color[0], color[1], color[2]
			fg = f'\033[38;2;{r};{g};{b}m'
			col_array.append(fg)

		for color in right_colors:
			r, g, b = color[0], color[1], color[2]
			fg = f'\033[38;2;{r};{g};{b}m'
			col_array.append(fg)

	  
		for character in string: 
			if base_iter == len(col_array):
				break
		  
			base_string += "" + col_array[base_iter] + character 
			base_iter += 1
		

		string = base_string + "\x1b[39m"
		return string
