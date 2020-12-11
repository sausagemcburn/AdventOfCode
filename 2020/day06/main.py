'''
Day 6, 2020

 Find what kinda questions each group answered yes

Strat:
 1. make a list of dictionaries
 2. each entry in list represents a group
 3. each entry is a dict which represents answers
   { 'a': True, 'b': True } etc.
 4. lengths of these 
'''


import sys
# import util module
sys.path.insert(1, '../../util/')
import helper


if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = helper.parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)

	# open input file object
	fo = open(puzzle_input)

	# iterate through groups, collect answers
	answers = {}
	groups = []
	grp = []
	for ans in fo:
		if ans == '\n':
			# group is over 
			if part == 1:
				groups.append(answers)
				answers = {}
			else:
				groups.append(grp)
				grp = []


		ans = ans.strip()

		if part == 1:
			for char in ans:
				answers[char] = True
		else:
			for char in ans:
				answers[char] = True
			if answers != {}:
				grp.append(answers)
			answers = {}


	
	if part == 1:
		# append the last answer
		groups.append(answers)
		# count length of each dict
		#  this equates to number of answers 'Yes'
		total = 0
		for g in groups:
			total += len(g)

		print 'total (part 1): ', total

	else:
		# part 2, check for questions EVERYONE answered
		total = 0

		# append the last grp
		groups.append(grp)
		print groups 

		# iterate through each group
		for grp in groups:
			print 'grp: ', grp
			# generate a histogram based on first person's answers
			histo = grp[0]
			i = 1
			# check histogram against all other answers
			while i < len(grp):
				for answer in histo.keys():
					# if the answer isnt in the keys of the other ppl
					#  then set it to false
					if answer not in grp[i].keys():
						histo[answer] = False
				i += 1

			# now check which ones are still True
			print 'histo: ', histo
			for k in histo.keys():
				if histo[k]:
					total += 1

		print 'total (part 2): ', total

	exit()
