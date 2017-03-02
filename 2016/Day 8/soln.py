import re

RECT_RULE = 1
ROT_ROW_RULE = 2
ROT_COL_RULE = 3

def rect_rule(screen, col, row):
	for idx in range(row):
		for jdx in range(col):
			screen[idx][jdx] = 1


def rot_row_rule(screen, row, rotation):
	row_len = len(screen[0])
	if rotation >= row_len:
		rotation = rotation % row_len

	holder = [None for idx in range(row_len)]
	for idx in range(row_len):
		curr_val = screen[row][idx]
		new_pos = (idx + rotation)%row_len
		holder[new_pos] = curr_val


	for idx in range(row_len):
		screen[row][idx] = holder[idx]

def rot_col_rule(screen, col, rotation):
	col_len = len(screen)
	if rotation >= col_len:
		rotation = rotation % col_len

	holder = [None for idx in range(col_len)]
	for idx in range(col_len):
		curr_val = screen[idx][col]
		new_pos = (idx + rotation)%col_len
		holder[new_pos] = curr_val

	for idx in range(col_len):
		screen[idx][col] = holder[idx]

def determine_rule(rule):
	if rule.startswith('rect'):
		pattern = '(\d+)x(\d+)'
		match = re.search(pattern, rule)
		if not match:
			raise Exception("Invalid RECT rule")
		rule_type = RECT_RULE
		rule_values = [int(match.group(1)), int(match.group(2))]
	elif rule.startswith('rotate'):
		pattern = '(\w)=(\d+) by (\d+)'
		match = re.search(pattern, rule)
		if not match:
			raise Exception("Invalid ROTATE rule")

		row_or_column = match.group(1)
		if row_or_column == 'y':
			rule_type = ROT_ROW_RULE
		elif row_or_column == 'x':
			rule_type = ROT_COL_RULE
		else:
			raise Exception("Invalid ROTATE rule")

		rule_values = [int(match.group(2)), int(match.group(3))]
		
	else:
		raise Exception("Invalid rule")

	return rule_type, rule_values

def get_lit_screen_count(screen):
	lit = 0
	for row in screen:
		lit += sum(row)
	return lit

def process_rules(rules):
	screen = [[0 for idx in range(50)] for idx in range(6)]
	for rule in rules:
		rule = rule.strip()
		rule_type, rule_values = determine_rule(rule)

		if rule_type == RECT_RULE:
			rect_rule(screen, rule_values[0], rule_values[1])
		
		elif rule_type == ROT_COL_RULE:
			rot_col_rule(screen, rule_values[0], rule_values[1])

		elif rule_type == ROT_ROW_RULE:
			rot_row_rule(screen, rule_values[0], rule_values[1])

		else:
			raise Exception("Invalid rule data")

	return screen

def print_screen(screen):
	for row in screen:
		line = ""
		for idx in range(len(row)):
			if idx>0 and idx%5 == 0:
				line += '|'

			if row[idx] == 1:
				line += '#'
			else:
				line += ' '
		print line

	


if __name__ == "__main__":
	input_file = open("input.txt", "r")
	rules = input_file.readlines()
	screen = process_rules(rules)
	lit_count = get_lit_screen_count(screen)
	
	print "%d pixels should be lit" %lit_count

	print_screen(screen)

