#  File: Dice.py
#  Description: Dice game simulation
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 
#
#  Date Created: 9/15/2017
#  Date Last Modified: 09/15/2017


import random

#Various functions

def countrolls(rolls):
	

	# initialize counts
	counts = {}
	for i in range(2, 13):
		counts[i] = 0

	#going through rolls, adding freq to counts
	for r in rolls:
		counts[r] += 1

	return counts

def generatedicerolls(n):
	
	
	rolls = []

	#creating n dice rolls, appending the sum into rolls list.
	while(n):
		D1 = random.randint(1,6)
		D2 = random.randint(1,6)
		D = D1 + D2
		rolls.append(D)
		
		n -= 1

	
	return countrolls(rolls)

def scaledicerolls(rolls, n):
    #scaling the rolls using the given formula

	if (n > 100):
		for i in rolls:
			rolls[i] = round(rolls[i]*(100/n))

	return rolls

def convertFreqData(freq):
	
	data = []

	
	maxx = max(list(freq.values()))

	
	while(maxx):

		
		lineData = list(freq.values())
		data.append(lineData)

		
		for f in freq:
			if(freq[f] > 0):
				freq[f] -= 1

		maxx -= 1

	
	data.reverse()
	return data


def printhistogramline(lis):
	
	print("|", end="")
	for x in lis:
		# padding
		print("  ", end="")
		#if no value, print a blank space, else print an asterisk
		if(x == 0):
			print(" ", end="")
		else:
			print("*", end="")
	
	print()

def printhistogram(freq):
	
        #printing given data as a dictionary
	
	freq = convertFreqData(freq)
	
	for f in freq:
		printhistogramline(f)

	#x axis
	print("+--+--+--+--+--+--+--+--+--+--+--+-")
	#numberings according to estimated spaces required
	print("   2  3  4  5  6  7  8  9 10 11 12")
	print()




def main():

	#using the given seed value.	
	random.seed(1314)

	
	print()
	n = int(input("How many times do you want to roll the dice? "))
	rolls = generatedicerolls(n)

	
	print("Results ", list(rolls.values()))
	print()

	
	rolls = scaledicerolls(rolls, n)
	printhistogram(rolls)




main()
