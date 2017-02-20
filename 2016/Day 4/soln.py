import re
from collections import Counter

def get_most_common(encrypted_name):
	most_common = Counter(encrypted_name).most_common()
	commonest = ''
	commonest_group = []
	count = 1
	rating = most_common[0][1]
	for item in most_common:
		item_rating = item[1]
		if item_rating < rating:
			rating = item_rating
			commonest_group.sort()
			for char in commonest_group:
				commonest += char
				if len(commonest) == 5:
					return commonest

			commonest_group = []
			commonest_group.append(item[0])


		else:
			commonest_group.append(item[0])

	if len(commonest) <5:
		commonest_group.sort()
		for char in commonest_group:
			commonest += char
			if len(commonest) == 5:
				break


	return commonest

def is_real_room(encrypted_name, checksum):
	commonest = get_most_common(encrypted_name)
	commonest = set(commonest)
	set_checksum = set(checksum)
	diff = set_checksum - commonest
	is_real = len(diff) == 0
	return is_real

def sum_real_rooms(rooms):
	room_sum = 0
	for room in rooms:
		room_sum += room[0]
	return room_sum


def get_real_rooms(rooms):
	real_rooms = []
	for room in rooms:
		room = room.strip()
		pattern = '([\w-]+)-(\d+)\[(\w+)\]'
		match = re.match(pattern, room)
		encrypted_name = match.group(1).replace("-", "")
		sector_id = int(match.group(2))
		checksum = match.group(3)
		if is_real_room(encrypted_name, checksum):
			real_rooms.append([sector_id, encrypted_name, checksum])
	return real_rooms

def unencrypt_name(encrypted_name, sector_id):
	unencrypted = ""
	for char in encrypted_name:
		ascii_idx = ord(char)
		new_ascii_idx = ascii_idx + sector_id%26
		if new_ascii_idx > ord('z'):
			new_ascii_idx = ord('a') - 1 + new_ascii_idx - ord('z')
		unencrypted += chr(new_ascii_idx)
	return unencrypted

if __name__ == '__main__':
	input_file = open("input.txt", "r")
	rooms = input_file.readlines()
	# rooms = [
	# 	'aaaaa-bbb-z-y-x-123[abxyz]',
	# 	'a-b-c-d-e-f-g-h-987[abcde]',
	# 	'not-a-real-room-404[oarel]',
	# 	'totally-real-room-200[decoy]'
	# ]
	real_rooms = get_real_rooms(rooms)
	sum_sector_id = sum_real_rooms(real_rooms)
	print "The sum of the sector IDS is ", sum_sector_id

	for room in real_rooms:
		print unencrypt_name(room[1], room[0]), room[0]