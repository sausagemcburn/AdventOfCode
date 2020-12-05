'''
Day 1 2019
 Calculating fuel necessary based on mass

Strat:
 1. read each number, do the maths
 2. EZ Clapperino
'''

import sys


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


def calculateFuel(mass):
	# recursively calculate fuel based on mass of fuel and ship
	if mass < 9: 
		return 0
	else:
		fuel = (mass / 3) - 2
		return fuel + calculateFuel(fuel)

if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
		
	# open input file object
	fo = open(puzzle_input)

	fuel = 0
	for mass in fo:
		mass = mass.strip()
		if part == 1:
			fuel += (int(mass) / 3) - 2
		else:
			new_fuel = calculateFuel(int(mass))
			fuel += new_fuel
			print new_fuel
	
	print 'fuel needed: ', fuel

	exit()
