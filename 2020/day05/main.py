'''
Day 5

 Find your seat on the plane cause u stupid

Strat:
 1. IF its a F or B split it one way
 2. If its a R or L split it one way
 3. EZ Clap 2 EZ GodGamer
'''

import sys
import re


def parseCmdLineArgs(argv, test, puzzle, pt):
	# default args are passed in
	if len(argv) > 3:
		throwError(0)
	elif len(argv) == 3: 
		if argv[1].lower() != '-test':
			throwError(1)
		puzzle = test
		if argv[2].lower() != '-part2':
			throwError(2)
		pt = 2
	elif len(argv) == 2:
		if argv[1].lower() != '-part2' and argv[1].lower() != '-test':
			throwError(3)
		if argv[1].lower() == '-test':
			puzzle = test
		else:
			pt = 2
	return puzzle, pt


def throwError(code = -1):
	print 'ILLEGAL'
	if code == 0:
		print 'too many cmd line args'
	elif code == 1:
		print 'wrong 1st cmd line arg. try -test'
	elif code == 2:
		print 'wrong 2nd cmd line arg. try -part2'
	elif code == 3:
		print 'wrong cmd line arg. try -part2 or -test'
	exit()



	

if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
		
	# open input file object
	fo = open(puzzle_input)


	highest = 0
	seats = []
	for line in fo:
		line = line.strip()
		# keep track of extents
		a, b = 0, 127
		x, y = 0, 7
		# keep track of width of range
		row = len(range(a, b+1))
		col = len(range(x, y+1))

		# loop through the commands/directions
		for c in line:
			if c == 'F':
				b -= row / 2
				row = len(range(a, b+1))
			if c == 'B':
				a += row / 2
				row = len(range(a, b+1))
			if c == 'L':
				y -= col / 2
				col = len(range(x, y+1))
			if c == 'R':
				x += col / 2
				col = len(range(x, y+1))

		# calculate seat number
		seat = a * 8 + x
		if part == 2:
			seats.append(seat)
		# is it the highest?
		if seat > highest:
			highest = seat 

	# print highest if part one
	if part == 1:
		print 'highest: ', str(highest)

	# if part two, find seat number
	if part == 2:
		my_seat = 0
		seats.sort()
		i = 0
		# iterate through all possible seat numbers, s
		for s in range(seats[0], seats[-1] + 1):
			# once theres a discrepancy, s is my seat
			if seats[i] != s:
				my_seat = s
				break
			i += 1

		print 'my seat: ' + str(my_seat)


	

	exit()
