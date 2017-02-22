import re
import math

def is_abba(sequence):
	if len(sequence) != 4:
		return False
	first_half = sequence[0:2]
	second_half = sequence[2:]
	if first_half == second_half:
		return False

	if first_half[0] == second_half[1] and first_half[1] == second_half[0]:
		return True

	return False

def is_aba_or_bab(sequence):
	if len(sequence) != 3:
		return False

	return sequence[0] == sequence[2]


def sequence_has_abba(sequence):
	has_abba = False
	rdx_slice = 0
	ldx_slice = 4
	while ldx_slice <= len(sequence):
		sliced = sequence[rdx_slice: ldx_slice]
		has_abba = is_abba(sliced)
		if has_abba:
			break
		rdx_slice += 1
		ldx_slice += 1
	return has_abba

def get_bab_aba_sequences(sequence, is_bab=False):
	rdx_slice = 0
	ldx_slice = 3
	bab_aba_sequences = set([])
	while ldx_slice <= len(sequence):
		sliced = sequence[rdx_slice: ldx_slice]
	 	if is_aba_or_bab(sliced):
	 		if is_bab:
	 			bab_aba = "".join([sliced[1], sliced[0], sliced[1]])
	 			bab_aba_sequences.add(bab_aba)
	 		else:
	 			bab_aba_sequences.add(sliced)

	 	rdx_slice += 1
	 	ldx_slice += 1
	
	return bab_aba_sequences


def get_ip_sequences(ip_lines):
	sequences = []
	for line in ip_lines:
		line = line.strip()
		pattern_1 = "\[(\w+)\]"
		pattern_2 = "\[\w+\]"
		sequences.append({
			"hypertext_sequence": re.findall(pattern_1, line),
			"supernet_sequence": re.split(pattern_2, line)
		})

	return sequences

def supports_tls(ip_sequence):
	for sequence in ip_sequence['hypertext_sequence']:
		if sequence_has_abba(sequence):
			return False

	for sequence in ip_sequence['supernet_sequence']:
		if sequence_has_abba(sequence):
			return True

	return False

def supports_ssl(ip_sequence):
	bab_sequences = set([])
	for sequence in ip_sequence['supernet_sequence']:
		bab_sequence = get_bab_aba_sequences(sequence, True)
		bab_sequences = bab_sequences | bab_sequence


	for sequence in ip_sequence['hypertext_sequence']:
		aba_sequence = get_bab_aba_sequences(sequence)
		if len(aba_sequence & bab_sequences) > 0:
			return True

	return False


def get_ip_tls_support_count(ip_sequences):
	count = 0
	for ip in ip_sequences:
		if supports_tls(ip):
			count += 1
	return count

def get_ip_ssl_support_count(ip_sequences):
	count = 0
	for ip in ip_sequences:
		if supports_ssl(ip):
			count += 1
	return count

if __name__ == "__main__":
	input_file = open("input.txt", "r")
	ip_lines = input_file.readlines()
	ip_sequences = get_ip_sequences(ip_lines)
	tls_support_count = get_ip_tls_support_count(ip_sequences)
	print "%d IP Addresses support TLS" %tls_support_count
	# ssl_sequences = [{
	# 	'hypertext_sequence': ['bab'],
	# 	'supernet_sequence': ['aba', 'xyz']
	# }, {
	# 	'hypertext_sequence': ['xyx'],
	# 	'supernet_sequence': ['xyx', 'xyx']
	# }, {
	# 	'hypertext_sequence': ['bzb'],
	# 	'supernet_sequence': ['zazbz', 'cdb']
	# }]
	#
	
	ssl_support_count = get_ip_ssl_support_count(ip_sequences)
	print "%d IP Addresses support SSL" %ssl_support_count