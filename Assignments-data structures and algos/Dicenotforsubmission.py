#  File: Dice.py
#  Description: Dice game simulation
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 01/27/2017
#  Date Last Modified: 01/29/2017

# import statements

import random



# functions

def countRolls(rolls):
	

	# initialize counts
	counts = {}
	for i in range(2, 13):
		counts[i] = 0

	# iterate through rolls, adding the frequency to counts
	for r in rolls:
		counts[r] += 1

	return counts

def generateDiceRolls(n):
	'''
	Generage n dice rolls
	'''

	# create array to hold the rolls
	rolls = []

	# create n dice rolls
	while(n):
		# simluate two dice and add them together
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		d = d1 + d2
		# add the new dice total
		rolls.append(d)
		# decrement by 1
		n -= 1

	# use countRolls to count the frequency of all the rolls
	return countRolls(rolls)

def scaleDiceRolls(rolls, n):
	'''
	scale the dice rolls using the formula (rounded results): outcomes * (100/trials)
	'''

	if (n > 100):
		for i in rolls:
			rolls[i] = round(rolls[i]*(100/n))

	return rolls

def convertFreqData(freq):
	'''
	conver the frequency data (dictionary) 2D list representing each line of the histogram
	'''
	data = []

	# get max frequency. This function assumes that there is postive max in the fequency
	m = max(list(freq.values()))

	# itterate through the list m times to generate the data
	while(m):

		# get the current frequency data and append it to data
		lineData = list(freq.values())
		data.append(lineData)

		# decrease all values greater than 0 by one
		for f in freq:
			if(freq[f] > 0):
				freq[f] -= 1

		m -= 1

	# reverse the data so it's in the right order
	data.reverse()
	return data


def printHistogramLine(lis):
	'''
	print a single line of the histogram given frequency data
	'''
	# print a bar for y-axis
	print("|", end="")
	for x in lis:
		# padding
		print("  ", end="")
		#if no value, print a blank space, else print an asterisk
		if(x == 0):
			print(" ", end="")
		else:
			print("*", end="")
	# print a new line
	print()

def printHistogram(freq):
	'''
	print a histogram given frequency data recieved as a dictionary
	note: this histogram has hardcoded x-axis and scale since it is being used for a specific problem
	'''

	# convert the freq data to be interpreted by printHistogramLine
	freq = convertFreqData(freq)
	# itterate through the data and print the lines
	for f in freq:
		printHistogramLine(f)

	# print the x-axis with ticks
	print("+--+--+--+--+--+--+--+--+--+--+--+-")
	# print the bins
	print("   2  3  4  5  6  7  8  9 10 11 12")
	print()

# end functions


def main():
	'''
	Program prompts the user for the number of dice rolls he/she wants to simulate,
	then displays the outcome as both a list and a histogram.
	'''

	# set the seed for random
	random.seed(1314)

	# receive number of dice rolls from user
	print()
	n = int(input("How many times do you want to roll the dice? "))
	rolls = generateDiceRolls(n)

	# print the counts for each value, ordered 2 through 12
	print("Results ", list(rolls.values()))
	print()

	# scale the rolls and print the histogram
	rolls = scaleDiceRolls(rolls, n)
	printHistogram(rolls)


# run the main function`
if __name__ == "__main__":
	main()
