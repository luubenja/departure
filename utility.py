block_size = 50
screen_width = 1000
screen_height = 500
blocks_per_row = screen_width / block_size

def convert_coordinates_to_grid(x,y):
	grid_num = (y / block_size)*(blocks_per_row) + x / block_size
	offset_x = x % block_size
	offset_y = y % block_size
	return [grid_num, offset_x, offset_y]