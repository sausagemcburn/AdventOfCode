#!/usr/bin/env python3

'''
Day 8, 2020

 catch the program once it infinitely loops

Strat:
 1. load whole program into list of class objs
 2. class will be Instruction
 3. boolean keeps track of if instruction has been run
'''


import sys
# import util module
sys.path.insert(1, '../../util/')
import helper3


class Instruction():

	op = 'nop'
	arg = 0
	complete = False

	def __init__(self, operation, argument):
		self.op = operation
		if argument[0] == '+':
			self.arg = int(argument[1:])
		else:
			self.arg = -1 * int(argument[1:])
		return

	def run(self):
		self.complete = True
		return

	def isRun(self):
		return self.complete

	def getOp(self):
		return self.op

	def getArg(self):
		return self.arg

	def changeOp(self):
		if self.op == 'jmp':
			self.op = 'nop'
		else:
			self.op = 'jmp'
		return

	def reset(self):
		self.complete = False
		return


def tryProgram(p):
	acc = 0
	i = 0
	while True:
		if i == len(p):
			return True, acc
		elif i > len(p):
			return False, acc

		if program[i].isRun():
			return False, acc

		program[i].run()

		if program[i].getOp() == 'acc':
			acc += program[i].getArg()
			i += 1
		elif program[i].getOp() == 'jmp':
			i += program[i].getArg()
		else:
			i += 1


if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = helper3.parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
	
	# open input file object
	fo = open(puzzle_input)

	# read instructions into program list
	program = []
	for i in fo:
		i = i.strip()
		i = i.split()
		inst = Instruction(i[0], i[1])
		program.append(inst)
	

	if part == 1:
		success, accumulator = tryProgram(program)
	else:
		# part 2, test each instruction changed
		for inst in program:
			if inst.getOp() == 'nop' or inst.getOp() == 'jmp':
				inst.changeOp()
				success, accumulator = tryProgram(program)
				if success:
					# nice job, leave loop
					print('success!')
					break
				else:
					# this wasnt it, change everything back
					inst.changeOp()
					for i in program:
						i.reset()



	print(f'accumulator value (part {part}): {accumulator}')

	exit()
