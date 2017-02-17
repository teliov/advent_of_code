#! /usr/bin/env python
import re

HOR_ORIENTATION = 0
VERT_ORIENTATION = 1
LEFT_DIR = 0
RIGHT_DIR = 1

def add_coord(coord1, coord2):
	x = coord1[0] + coord2[0]
	y = coord1[1] + coord2[1]
	return (x, y)

def list_points(coord1, coord2):
	points = []
	x1 = coord1[0]
	y1 = coord1[1]
	x2 = coord2[0]
	y2 = coord2[1]

	if x1 == x2:
		is_negative = y1 > y2
		for idx in range(abs(y1-y2)):
			adv = idx if not is_negative else -1*idx
			points.append((x1, y1+adv))
		return points

	if y1 == y2:
		is_negative = x1 > x2
		for idx in range(abs(x1-x2)):
			adv = idx if not is_negative else -1*idx
			points.append((x1+adv, y1))
		return points

	return points

def is_right(direction):
	return direction == RIGHT_DIR

def is_horizontal(orientation):
	return orientation == HOR_ORIENTATION

def get_resultant_distance(instructions):
	coords_list = [(0,0)]
	visited = set([])
	has_visited_again = False
	distance_to_visit = 0
	current_orientation = HOR_ORIENTATION
	dir_indicator = 1
	current_direction = None
	for instruction  in instructions :
		match = re.match('(\w)(\d+)', instruction)
		if match == None:
			raise Exception("Invalid data")

		distance = int(match.group(2))
		current_direction = RIGHT_DIR if (match.group(1) == 'R') else LEFT_DIR
		
		if is_right(current_direction) and is_horizontal(current_orientation):
			advance_coord = (distance*dir_indicator, 0)
		elif is_right(current_direction) and not is_horizontal(current_orientation):
			dir_indicator = -1*dir_indicator
			advance_coord = (0, distance*dir_indicator)
		elif not is_right(current_direction) and is_horizontal(current_orientation):
			dir_indicator = -1*dir_indicator
			advance_coord = (distance*dir_indicator, 0)
		else:
			advance_coord = (0, distance*dir_indicator)

		current_orientation = HOR_ORIENTATION if current_orientation == VERT_ORIENTATION else VERT_ORIENTATION

		
		old_coord = coords_list[len(coords_list) - 1]
		new_coord = add_coord(advance_coord, old_coord)
		points_visited = list_points(old_coord, new_coord)
		if not has_visited_again:
			for point in points_visited:
				if not point in visited:
					visited.add(point)
				else:
					distance_to_visit = abs(point[1]) + abs(point[0])
					has_visited_again = True
		coords_list.append(new_coord)
		

	return abs(new_coord[0]) + abs(new_coord[1]), distance_to_visit

def get_instructions(instruction_string):
	instructions = instruction_string.split(", ")
	return instructions

if __name__ == '__main__':
	input_file = open("input.txt", "r")
	input_string =  input_file.readline()
	instructions = get_instructions(input_string)
	resultant_distance, distance_to_visit = get_resultant_distance(instructions)
	print "resultant_distance: ", resultant_distance
	print "distance_to_visit: ", distance_to_visit