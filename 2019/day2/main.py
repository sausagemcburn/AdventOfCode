'''
Day 2 2019
 reading a program, scratchin my underarm fungus, 
 lookin for opcodes

Strat:
 1. read each number, look for opcodes
 2. when you find opcode, do it, then +4
 3. EZ Clapperino
'''

import sys
# import helper module
sys.path.insert(1, '../../util/')
import helper

def operation(opcode, x, prog):
	if opcode == 1:
		prog[prog[x+3]] = prog[prog[x+1]] + prog[prog[x+2]]
	elif opcode == 2:
		prog[prog[x+3]] = prog[prog[x+1]] * prog[prog[x+2]]
	return prog

def runProgram(prog):

	# run the prog, perform operations and increment 
	i = 0 
	while True:
		if prog[i] == 1:
			prog = operation(1, i, prog)
			i += 4
		elif prog[i] == 2:
			prog = operation(2, i, prog)
			i += 4
		elif prog[i] == 99:
			break
		else:
			i += 1

	return prog

if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = helper.parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
		
	# open input file object
	fo = open(puzzle_input)

	# bring program into a list
	program = map(int, fo.read().split(','))

	if part == 1:
		# do the 1202 thingy
		program[1] = 12
		program[2] = 2
		program = runProgram(program)
	else:
		# part 2
		# keep trying nouns and verbs until we have the number
		finished = False
		for x in range(100):
			for y in range(100):
				prg_copy = program[:]
				prg_copy[1] = x
				prg_copy[2] = y
				prg_copy = runProgram(prg_copy)
				if prg_copy[0] == 19690720:
					print 'noun: ', x
					print 'verb: ', y
					print 'product: ', 100 * x + y
					program = prg_copy[:]
					finished = True
					break

			if finished:
				break


	

	print program

	exit()
