'''
Day 4
 Checking passport metadata or something
 The input file is all fucky though

Strat:
 1. loop through file by line
 2. keep track of separators
 3. after you find a separator, check the data
 4. EZ Clap??? 
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




def confirmValidPP(pp, pt):
	# valid if there are 8 fields
	#  or 7 fields and the only missing one is 'cid'
	# send a 1 back if valid, 0 if not
	if len(pp) < 8:
		if 'cid' not in pp.keys() and len(pp) == 7:
			if pt == 1:
				return 1
		else:
			return 0

	if pt == 1:
		return 1

	# ok so if we get here, we have the right amount of fields
	# now to check validity of each

	# byr
	# just has to be a 4-digit number btwn two other numbers
	#  same with the next two categories
	if not pp['byr'].isdigit() or len(pp['byr']) != 4:
		return 0
	if int(pp['byr']) < 1920 or int(pp['byr']) > 2002:
		return 0

	# iyr
	if not pp['iyr'].isdigit() or len(pp['iyr']) != 4:
		return 0
	if int(pp['iyr']) < 2010 or int(pp['iyr']) > 2020:
		return 0

	# eyr
	if not pp['eyr'].isdigit() or len(pp['eyr']) != 4:
		return 0
	if int(pp['eyr']) < 2020 or int(pp['eyr']) > 2030:
		return 0

	# hgt 
	# has to have cm or in at the end
	if pp['hgt'][-2:] != 'cm' and pp['hgt'][-2:] != 'in':
		return 0
	units = pp['hgt'][-2:]
	# rest of it must be a number btwn two other numbers
	if not pp['hgt'][:-2].isdigit():
		return 0
	if units == 'cm':
		if int(pp['hgt'][:-2]) < 150 or int(pp['hgt'][:-2]) > 193:
			return 0
	elif units == 'in':
		if int(pp['hgt'][:-2]) < 59 or int(pp['hgt'][:-2]) > 76:
			return 0

	# hcl
	# just gonna use a regex for this
	# needs to be a color hex code
	# just found one here:
	# https://stackoverflow.com/questions/30241375/python-how-to-check-if-string-is-a-hex-color-code
	if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', pp['hcl']):
		return 0

	# ecl 
	# just gotta be one of the valid ones in this list
	eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if pp['ecl'] not in eye_colors:
		return 0

	# pid
	# 9 digit number include leading zeros
	if len(pp['pid']) != 9 or not pp['pid'].isdigit():
		return 0 

	# if you made it here, you're legit! 
	return 1


	

if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
		
	# open input file object
	fo = open(puzzle_input)

	# loop through each line of the file
	currentpp = {}
	validpps = 0
	for line in fo:
		
		if line == '\n':
			# this is a separator line
			#  confirm valid data
			for k in currentpp.keys():
				print k, currentpp[k]
			print ' '
			validpps += confirmValidPP(currentpp, part)
			print validpps
			print ' '
			currentpp = {}
			continue

		# pull the data out of the line if there is any
		templine = line.strip().split()
		temppair = []

		for pair in templine:
			currentpp[pair[:3]] = pair[4:]
		
	# even though we're out of the loop,
	#  we still havent checked the last entry
	print currentpp
	validpps += confirmValidPP(currentpp, part)

	print 'Valid Passports: ' + str(validpps)

	exit()
