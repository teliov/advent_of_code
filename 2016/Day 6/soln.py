def get_alpha_count(lines):
	num_columns = len(lines[0].strip())
	alpha_count = [[None for idx in range(26)] for idx in range(num_columns)]

	for line in lines:
		line = line.strip()
		for idx in range(len(line)):
			char = line[idx]
			alpha_idx = ord(char) - 97
			if alpha_count[idx][alpha_idx]:
				alpha_count[idx][alpha_idx] += 1
			else:
				alpha_count[idx][alpha_idx] = 1
	return alpha_count

def unjam_input(lines):
	alpha_count = get_alpha_count(lines)
	rearranged = ''
	for count in alpha_count:
		max_count = 0
		max_char = 'a'
		for idx in range(len(count)):
			val = count[idx]
			if val is not None and val > max_count:
				max_count = val
				max_char = chr(97 + idx)

		rearranged += max_char

	return rearranged

def unjam_input_pt2(lines):
	alpha_count = get_alpha_count(lines)
	rearranged = ''
	for count in alpha_count:
		min_count = len(lines)
		min_char = 'a'
		for idx in range(len(count)):
			val = count[idx]
			if val is not None and val < min_count:
				min_count = val
				min_char = chr(97 + idx)

		rearranged += min_char

	return rearranged

if __name__ == "__main__":
	input_file = open("input.txt", "r")
	lines = input_file.readlines()
	# lines = [
	# 	'eedadn',
	# 	'drvtee',
	# 	'eandsr',
	# 	'raavrd',
	# 	'atevrs',
	# 	'tsrnev',
	# 	'sdttsa',
	# 	'rasrtv',
	# 	'nssdts',
	# 	'ntnada',
	# 	'svetve',
	# 	'tesnvt',
	# 	'vntsnd',
	# 	'vrdear',
	# 	'dvrsen',
	# 	'enarar'
	# ]
	unjammed = unjam_input(lines)
	print "unjammed input is ", unjammed
	unjammed = unjam_input_pt2(lines)
	print "unjammed input (pt2) is ", unjammed