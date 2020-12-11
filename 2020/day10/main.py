#!/usr/bin/env python3

'''
Day 10, 2020

 Reading in a list of joltages, sorting
 Taking histogram of joltage differences

Strat:
 1. sort da list 
 2. run through it and make a histogram
'''



import sys
# import util module
sys.path.insert(1, '../../util/')
import helper3



def generateHistogram(dptrs):
	h = {
		1: 0,
		2: 0,
		3: 0
	}
	for i in range(len(dptrs)):
		h[dptrs[i+1] - dptrs[i]] += 1
		if i + 2 >= len(dptrs):
			break

	return h



def generateTree(dptrs):
	t = {}
	b = { 0: True }
	for i in range(len(dptrs)):
		if i + 1 >= len(dptrs):
			break
		# add the next dptr in sequence always
		t[dptrs[i]] = []
		t[dptrs[i]].append(dptrs[i+1])
		# check and see if the next two can be added
		for j in range(2,4):
			if i+j >= len(dptrs):
				break
			if dptrs[i+j] - dptrs[i] <= 3:
				t[dptrs[i]].append(dptrs[i+j])

		# if there is only 1 value in the list corresponding
		#  to the current dapter, that value is:
		#   a. next in the dapters list
		#   b. necessary for the chain
		b[dptrs[i+1]] = (len(t[dptrs[i]]) == 1)

	return b


def calculateArrangements(p):
	i = 0
	dptrs = list(p.keys())
	streak = 1
	combos = 1
	# done = False
	while i < len(dptrs):
		if not p[dptrs[i]]:
			# this is an unnecessary piece
			# start the streak
			i += 1
			while not p[dptrs[i]]:
				streak += 1
				if i + 1 >= len(dptrs):
					# done = True
					break
				i += 1

			# streak is done
			# current p[dptr[i]] is valid (True)
			# factor combos = fibInt up to streak length
			factor_combos = fibonacciIntegral(streak)
			combos *= factor_combos
			streak = 1

		i += 1

	return combos


def fibonacciIntegral(idx):
	total = 0
	for i in range(idx+1):
		total += fib(i)
	return total


# i is index in fibonacci sequence
def fib(i):
	if i <= 1:
		return 1
	return fib(i-1) + fib(i-2)



if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = helper3.parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
	
	# open input file object
	fo = open(puzzle_input)

	dapters = []
	for a in fo:
		a = a.strip()
		dapters.append(int(a))

	dapters.sort()

	# add the wall outlet and your device's adapter joltages
	dapters.insert(0, 0)
	dapters.append(dapters[-1] + 3)

	if part == 1:
		histo = generateHistogram(dapters)
		print('product:', histo[1] * histo[3])
	else:
		parts = generateTree(dapters)
		arrangements = calculateArrangements(parts)
		print('arrangements:', arrangements)
	
	exit()
