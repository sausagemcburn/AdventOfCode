'''
Day 2 
 You're entering the password on your toboggan or something
 Theres rules about valid passwords, find how many are valid

Strat:
 1. loop through the passwords and parse each line
 2. if valid, add to a counter
 3. EZ Clapperino
'''

# for cmd line args
import sys

test_input = 'test-input.txt'
puzzle_input = 'puzzle-input.txt'
part = 1


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
		
	# open input file object
	fo = open(puzzle_input)
	
	# reading each line in password file and counting
	total = 0
	for line in fo:
		line = line.strip()
		# set up some vars for checking passwords
		i, n, mini, maxi = 0, 0, 0, 0
		char, pwd = '', ''
		while True:
			# slowly take parts of the line that we need
			#  then just cut em off the line i guess
			i += 1
			if line[i] == '-':
				mini = int(line[:i])
				line = line[i+1:]
				i = 0
			elif line[i] == ' ' and maxi == 0:
				maxi = int(line[:i])
				char = line[i+1]
				pwd = line[i+4:]
				print str(mini), str(maxi), char, pwd
				break
			
		# check to make sure password follows the rules
		#  different rules for each part
		if part == 1:
			n = pwd.count(char)
			if n >= mini and n <= maxi:
				total += 1
		else:
			if (pwd[mini-1] == char) ^ (pwd[maxi-1] == char):
				total += 1


	print 'total (part ' + str(part) + '): ' + str(total)

	exit()
