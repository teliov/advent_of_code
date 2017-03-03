import re

def process_rules(storage, rules, process_queue, marker):
	special_bot = None
	while len(process_queue) > 0:
		bot_id = process_queue.pop()
		rule = rules[bot_id]
		chips = storage[bot_id]
		chips.sort()
		if chips == marker:
			special_bot = bot_id.split('_')[1]

		storage[bot_id] = []

		low_value = chips[0]
		high_value = chips[1]

		low_key = rule['low_dest_type'] + '_' + rule['low_dest']
		high_key = rule['high_dest_type'] + '_' + rule['high_dest']

		if not storage.has_key(low_key):
			storage[low_key] = [low_value]
		else:
			storage[low_key].append(low_value)

		if len(storage[low_key]) == 2:
			process_queue.append(low_key)

		if not storage.has_key(high_key):
			storage[high_key] = [high_value]
		else:
			storage[high_key].append(high_value)

		if len(storage[high_key]) == 2:
			process_queue.append(high_key)

	return special_bot

def process_instruction(instructions):
	storage = {}
	rules = {}
	process_queue = []
	for instruction in instructions:
		instruction = instruction.strip()
		
		if instruction.startswith('value'):
			pattern = 'value (\d+) goes to bot (\d+)'
			match = re.search(pattern, instruction)
			bot_id = 'bot_' + match.group(2)
			value = int(match.group(1))
			if not storage.has_key(bot_id):
				storage[bot_id] = [value]
			else:
				storage[bot_id].append(value)
			
			if len(storage[bot_id]) == 2:
				process_queue.append(bot_id)

		elif instruction.startswith('bot'):
			pattern = 'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'
			match = re.search(pattern, instruction)
			bot_id = 'bot_' + match.group(1)
			rule = {
				'low_dest_type': match.group(2),
				'low_dest': match.group(3),
				'high_dest_type': match.group(4),
				'high_dest': match.group(5)
			}
			if not rules.has_key(bot_id):
				rules[bot_id] = rule
			else:
				# two rules for a bot (erm no!)
				raise Exception("Invalid data: multiple rules for a bot")
			

		else:
			raise Exception("Invalid instruction")

	return storage, rules, process_queue



if __name__ == "__main__":
	input_file = open("input.txt", "r")
	instructions = input_file.readlines()
	marker = [17, 61]
	# instructions = [
	# 	'value 5 goes to bot 2',
	# 	'bot 2 gives low to bot 1 and high to bot 0',
	# 	'value 3 goes to bot 1',
	# 	'bot 1 gives low to output 1 and high to bot 0',
	# 	'bot 0 gives low to output 2 and high to output 0',
	# 	'value 2 goes to bot 2'
	# ]
	# marker = [2,5]
	storage, rules, process_queue = process_instruction(instructions)
	print process_rules(storage, rules, process_queue, marker)

	# for pt 2
	print storage['output_0'][0] * storage['output_1'][0] * storage['output_2'][0]
