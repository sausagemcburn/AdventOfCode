'''
Day 1   
 You're on a tropical island for xmas apparently
 PogChamp
 Something about expense reports or tax fraud or something though,
 Find which two numbers add to 2020, then multiply together

Strat:
 1. double loop through the numbers, check each pairs' sum
 2. if sum = 2020, multiply em together
 3. EZ Clapperino

Notes:
 Gonna make this run with an option on the cmd line for -test
 -test will trigger the use of test_input
 lack of -test uses puzzle_input
 Also gonna add an option for -part2
'''

# for cmd line args
import sys

test_input = 'test-input.txt'
puzzle_input = 'puzzle-input.txt'

def partTwo(tax_fraud):
	done = False
	for x in tax_fraud:
		for y in tax_fraud:
			for z in tax_fraud:
				if int(x) + int(y) + int(z) == 2020:
					product = int(x) * int(y) * int(z)
					done = True
					break
			if done:
				break
		if done: 
			break
	print 'product (part 2): ', product
	return


if __name__ == "__main__":
	# check input from cmd line
	if len(sys.argv) > 3:
		print 'ILLEGAL'
		print 'too many cmd line args'
		exit()
	elif len(sys.argv) == 3: 
		if sys.argv[1].lower() != '-test':
			print 'ILLEGAL'
			print 'wrong 1st cmd line arg. try -test'
			exit()
		puzzle_input = test_input
		if sys.argv[2].lower() != '-part2':
			print 'ILLEGAL'
			print 'wrong 2nd cmd line arg. try -part2'
			exit()
		part = 2
	elif len(sys.argv) == 2:
		if sys.argv[1].lower() != '-part2' and sys.argv[1].lower() != '-test':
			print 'ILLEGAL'
			print 'wrong cmd line arg. try -part2 or -test'
			exit()
		if sys.argv[1].lower() == '-test':
			puzzle_input = test_input
		else:
			part = 2
		

	# get numbers from the input file
	fs = open(puzzle_input, 'r')
	tax_fraud = fs.read()
	# now make it a list
	tax_fraud = tax_fraud.split('\n')

	# if part two, call function and exit
	if part == 2:
		partTwo(tax_fraud)
		exit()

	# else part one continues below

	# find the first two numbers that add to 2020
	done = False
	for x in tax_fraud:
		for y in tax_fraud:
			if int(x) + int(y) == 2020:
				done = True
				product = int(x) * int(y)
				break

		if done:
			break

	print 'product (part 1): ', product

	exit() 
