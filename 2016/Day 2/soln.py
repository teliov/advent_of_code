RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)


# for part 2
keypad = [
		[None, None, 1, None, None],
		[None, 2, 3, 4, None],
		[5, 6, 7, 8, 9],
		[None, "A", "B", "C", None],
		[None, None, "D", None, None]
]

def is_out_of_bound(point, bound):
	x1 =point[0]
	x2 = point[1]
	if x1 < 0 or x1 > bound:
		return True
	if x2 < 0 or x2 > bound:
		return True

	return False

def add_coord(coord1, coord2):
	x = coord1[0] + coord2[0]
	y = coord1[1] + coord2[1]
	return (x, y)


def get_code(instruction, start):
	pos = start
	instruction = instruction.strip()
	for move in instruction:
		old_pos = pos
		dir = None
		if move == 'R':
			dir = RIGHT
		elif move ==  'L':
			dir = LEFT
		elif move == 'U':
			dir = UP
		elif move == 'D':
			dir = DOWN
		else:
			raise Exception("Invalid data")

		new_pos = add_coord(pos, dir)
		if not is_out_of_bound(new_pos, 2):
			pos = new_pos

		#print "on: ", old_pos, " move to make: ", move, "now on ", pos

	return pos

def calc_value_from_pos(coord):
	return 3*coord[0] + coord[1] + 1

def solve_code(instructions):
	pos = (1, 1)
	code = ""
	for instruction in instructions:
		res = get_code(instruction, pos)
		#print "res ", res
		#print "#########"
		code += str(calc_value_from_pos(res))
		pos = res

	return code
def solve_code_pt2(instructions):
	pos = (3,2)
	code = ""
	for instruction in instructions:
		res = get_code_part_2(instruction, pos)
		#print "res ", res
		#print "#########"
		code += str(keypad[res[0]][res[1]])
		pos = res
	return code

def get_code_part_2(instruction, start):

	pos = start
	instruction = instruction.strip()
	for move in instruction:
		dir = None
		if move == 'R':
			dir = RIGHT
		elif move ==  'L':
			dir = LEFT
		elif move == 'U':
			dir = UP
		elif move == 'D':
			dir = DOWN
		else:
			raise Exception("Invalid data")

		new_pos = add_coord(pos, dir)
		if not is_out_of_bound(new_pos, 4) and keypad[new_pos[0]][new_pos[1]] is not None:
			pos = new_pos
	return pos

if __name__ == "__main__":
	input_file = open("input.txt", "r")
	instructions = input_file.readlines()
	#instructions = ['ULL','RRDDD','LURDL','UUUUD']
	code = solve_code(instructions)
	print "code is: " , code
	#print "###########"
	code = solve_code_pt2(instructions)
	print "code is: " , code
	