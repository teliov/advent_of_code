import hashlib
import re

def calculate_password(input_hash):
	password = ""
	index = 0
	while len(password) < 8:
		index_str = str(index)
		hash_str =  input_hash + index_str
		hex_str = hashlib.md5(hash_str).hexdigest()
		match = re.match('^00000(\w|\d)', hex_str)
		if match is not None:
			char = match.group(1)
			password += char
		index += 1

	return password

def calculate_password_pt2(input_hash):
	password = {}
	index = 0
	while len(password) < 8:
		index_str = str(index)
		hash_str =  input_hash + index_str
		hex_str = hashlib.md5(hash_str).hexdigest()
		match = re.match('^00000(\d)(\w|\d)', hex_str)
		if match is not None:
			pos = int(match.group(1))
			if pos < 8 and not password.has_key(pos):
				char = match.group(2)
				password[pos] = char
		index += 1

	password_str = ""
	for idx in range(0,8):
		password_str += password[idx]
	
	return password_str

if __name__ == '__main__':
	#input_hash = "abc"
	input_hash = "cxdnnyjw"
	password = calculate_password(input_hash)
	password_pt2 = calculate_password_pt2(input_hash)
	print "password is ", password
	print "pt2 password is", password_pt2