'''
Day 3
 You gotta BOGGAN baby!!!
 Gotta get down the hill at a certain slope

Strat:
 1. load the 'map' into a big multi-dimensional array
 2. use modulo for infinite map
 3. keep track of position and loop til u hit da bottom
 4. count up da treez
 4.20 EZ Clapperino

Notes: 
 Making a util module for some of these EZ clap functions
 Sub Note: 
  cant get this to work will try next time maybe
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

if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
		
	# open input file object
	fo = open(puzzle_input)

	# read in the tree map to a matrix
	#  in part one, we could optimize by just str8 up counting
	#  the trees here, but...whatever
	treemap = []
	for line in fo:
		treemap.append(line.strip())

	# create slopes variable by hand
	slopes = [
		[1, 1],
		[3, 1],
		[5, 1],
		[7, 1],
		[1, 2]
	]


	width = len(treemap[0])
	product = 1
	print 'slope:  \ttrees hit'
	for m in slopes:
		# tree counting variables; position, slope, count
		x, y = 0, 0
		mx, my = m[0], m[1]
		trees_hit = 0
		# while we dont overshoot the bottom
		while (y + my) < len(treemap):
			# increase position based on slope
			x += mx 
			y += my 
			if treemap[y][x % width] == '#':
				trees_hit += 1

		product *= trees_hit
		print '(' + str(mx) + ', ' + str(my) + '): \t' + str(trees_hit)

	print 'product: ' + str(product)

	exit()
