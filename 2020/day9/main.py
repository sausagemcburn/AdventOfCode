#!/usr/bin/env python3

'''
Day 9, 2020

 We get this preamble thing and
 We gotta check if the numbers coming after in order are valid
 Based on summed pairs of preamble

 Sigma 25 = 300
 

Strat:
 1. brute force it first ?? not sure
 2. operand pair key, sum value dictionary structure

dict = {
	(1, 25): 26,
	(2, 25): 27,
	etc 
}

'''



import sys
# import util module
sys.path.insert(1, '../../util/')
import helper3



def sumPreamble(l):
	# initial creation of sums dict
	sums = {}
	for i in range(len(l)):
		for j in range(len(l)):
			if j <= i:
				continue
			
			if l[i] < l[j]:
				coords = (l[i], l[j])
			else: 
				coords = (l[j], l[i])

			sums[coords] = l[i] + l[j]

	return sums


def checkSum(s, c):
	# check if the next number is in the sums values
	if c in s.values():
		return True
	return False


def regenSums(s, add_num, rm_num, p):
	# s = sums
	# add_num = number to add to sums dictionary
	# rm_num = number to remove from sums dict
	# p = current preamble minus add/rm nums

	# loop through preamble numbers
	# check preamble numbers + add/rm numbers against sums
	# rm where appropriate, then add

	for num in p:
		# remove the appropriate sum
		if num < rm_num:
			coords = (num, rm_num)
		else:
			coords = (rm_num, num)

		s.pop(coords)

		if num < add_num:
			coords = (num, add_num)
		else:
			coords = (add_num, num)

		s[coords] = num + add_num

	return s


if __name__ == "__main__":
	# default cmd line input vars
	test_input = 'test-input.txt'
	puzzle_input = 'puzzle-input.txt'
	part = 1

	# check input from cmd line
	puzzle_input, part = helper3.parseCmdLineArgs(sys.argv, test_input, puzzle_input, part)
	
	# open input file object
	fo = open(puzzle_input)


	# preamble length
	pre_len = 25

	# if test run, set different preamble length
	if puzzle_input == 'test-input.txt':
		pre_len = 5

	# read numbers file into ledger
	ledger = []
	for n in fo:
		n = n.strip()
		ledger.append(int(n))

	# loop forever
	i = 0
	sums = sumPreamble(ledger[i:pre_len+i])
	# print(len(sums))
	# print(sums)
	while True:
		
		check = checkSum(sums, ledger[i+pre_len])

		if not check:
			break

		sums = regenSums(sums, ledger[i+pre_len], ledger[i], ledger[i+1:i+pre_len])

		i += 1

		# iterate over preamble range
		#  check next number for validity
		# for j in range(i, pre_len + i):
			# if ledger

	# print(len(sums))
	# print(sums)
	# print(ledger[i+pre_len])
	# print(check)

	illegal = ledger[i+pre_len]
	print(f'illegal number: {illegal}')

	# check contiguous numbers in ledger for sum greater than
	#  or equal to the illegal number

	
	pre_len = i+1
	done = False
	while True:
		# iterate over ledger
		# print(pre_len)
		for i in range(len(ledger)):
			sexy_sum = sum(ledger[i:i+pre_len])
			# print(sexy_sum)
			if sexy_sum == illegal:
				done = True
				break

		if done:
			break

		pre_len -= 1


	weakness = min(ledger[i:i+pre_len]) + max(ledger[i:i+pre_len])

	print(f'weakness: {weakness}')

	
	exit()
