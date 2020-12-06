# helper.py
#  common functions 


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
