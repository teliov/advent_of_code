import re

def is_triangle_possible(sides):
	max_side = max(sides)
	sum_of_sides = sum(sides)

	diff = sum_of_sides - max_side
	return diff > max_side

def get_possible_triangles(triangles):
	possible_triangles = []
	for triangle in triangles:
		if is_triangle_possible(triangle):
			possible_triangles.append(triangle)
	return possible_triangles

def get_triangles_pt(triangles):
	triangle_list = []
	for triangle in triangles:
		triangle = triangle.strip()
		match = re.match('(\d+)\s+(\d+)\s+(\d+)', triangle)
		sides = [int(match.group(1)), int(match.group(2)), int(match.group(3))]
		triangle_list.append(sides)
	return triangle_list

def get_triangles_pt2(triangles):
	triangle_list = []
	count1 = []
	count2 = []
	count3 = []
	for triangle in triangles:
		triangle = triangle.strip()
		match = re.match('(\d+)\s+(\d+)\s+(\d+)', triangle)
		sides = [int(match.group(1)), int(match.group(2)), int(match.group(3))]
		
		count1.append(sides[0])
		count2.append(sides[1])
		count3.append(sides[2])

		
		if len(count1) == 3:
			triangle_list.append(count1)
			count1 = []
		if len(count2) == 3:
			triangle_list.append(count2)
			count2 = []
		if len(count3) == 3:
			triangle_list.append(count3)
			count3 = []
	return triangle_list



if __name__ == "__main__":
	input_file = open("input.txt", "r")
	triangles = input_file.readlines()
	#triangles = ['5 10 25', '3 4 5', '5 12 13']
	triangles_pt1 = get_triangles_pt(triangles)
	possible_triangles = get_possible_triangles(triangles_pt1);
	print "number of possible triangles are: ", len(possible_triangles)
	print "###########################"
	triangles_pt2 = get_triangles_pt2(triangles)
	possible_triangles = get_possible_triangles(triangles_pt2)
	print "number of possible triangles are: ", len(possible_triangles)