'''
Day 7, 2020

 Crazy data structure problem with bags n shit
 How many different bag colors can contain a gold bag?

Strat:
 1. dict of bags + contents
    {'tomato red': 
     	{'sky blue': 4,
     	'pea green': 2},
     'mellow yellow': {}
    }
 2. gonna be about parsing this input mostly
 3. check each color, then each sub color, until
     you either hit 
'''


import sys
# import util module
sys.path.insert(1, '../../util/')
import helper


def doesItHold(bd, b, t):
	# recursively check bags and sub-bags
	# lmao this is nutty will this even work?
	if bd[b].keys() == []:
		return 0
	elif t in bd[b].keys():
		return 1
	else:
		for k in bd[b].keys():
			if doesItHold(bd, k, t) == 1:
				return 1
		return 0


if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = helper.parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)

	# open input file object
	fo = open(puzzle_input)

	# construct directory of bags and what they hold
	bag_dir = {}
	for line in fo:
		line = line.strip()
		line = line.strip('.')
		line = line.split(' contain ')
		bagtype = line[0][:-5]

		if line[1] == 'no other bags':
			# this bag contains no bags
			bag_dir[bagtype] = {}
			continue

		# bags inside separated by comma
		contains = line[1].split(', ')
		temp_bags = {}

		# iterate through bags inside,
		# clean up text + keep track of number
		for bag in contains:
			bag = bag.strip()
			# get the number of bags
			for i in range(len(bag)):
				if bag[i] == ' ':
					num = int(bag[:i])
					bag = bag[i+1:]
					break
			if bag[-5:] == ' bags':
				bag = bag[:-5]
			else:
				bag = bag[:-4]

			temp_bags[bag] = num

		bag_dir[bagtype] = temp_bags
		

	# print bag_dir

	# now find how many of these bags can hold a shiny gold
	target = 'shiny gold'
	n = 0
	for bag in bag_dir.keys():
		n += doesItHold(bag_dir, bag, target)

	print 'bags that can hold shiny gold: ', n


	exit()
