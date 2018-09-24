#  File: ISBN.py

#  Description: Algorithm to validate vald ISBN numbers.

#  Student Name: Naman Mehra

#  Student UT EID: nm26465

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: April 15th, 2017

#  Date Last Modified: April 15th, 2017


def is_valid(ISBNno):
	#Function to check if ISBN is invalid
	if len(ISBNno) != 10:
		return False
	l = len(ISBNno)
	#Check if the first 9 characters are digits from 0-9
	for x in range(l-1):
		if ord(ISBNno[x]) <48 or ord(ISBNno[x])>57:
			return False
	#Check if the last character is x or X or a digit from 0-9
	if ISBNno[l-1] == 'x' or ISBNno[l-1] == 'X' or (ord(ISBNno[l-1])>48 and ord(ISBNno[l-1])<57):
		return True
	else:
		return False


def makelist(ISBNdigits):
	#convert ISBNdigits to list of digits
	list_of_numbers = []
	for char in ISBNdigits:
	#if last character is x or X, it is replaced by 10
		if char == 'x' or char == 'X':
			char = 10
		list_of_numbers.append(int(char))
	return list_of_numbers

def partialsums(digits):
	#compute partial sums s1 and s2. Return True if the last item in s2 is divisible by 11
	
	#initialize s1 and s2 to calculate partial sums
	s1 = [digits[0]]
	s2 = [s1[0]]

	#loop to calculate partial sums
	for x in range(1, len(digits)):
		s1.append(s1[x-1] + digits[x])
		s2.append(s2[x-1] + s1[x])

	#return result
	return s2[len(s2)-1]%11 == 0


def main():
	#open file to read
	readfile = open("ISBN.txt", "r")
	#open file to write
	write_file = open("isbnOut.txt", "w")

	#continue loop until the file reaches the end
	for ISBNno in readfile:
		#read the ISBN and strip newline character
		ISBNno = ISBNno.strip()
		#replace hyphens with null character
		ISBNdigits = ISBNno.replace("-", "")
		#Check if ISBN is valid
		if is_valid(ISBNdigits):
			#convert ISBN to a list of numbers
			digits = makelist(ISBNdigits)
			#compute partial sums and return if the ISBN is valid
			if partialsums(digits):
				#ISBN is valid
				output = format(ISBNno, "<13") + " valid\n" 
			else:
				#ISBN is not valid
				output = format(ISBNno, "<13") + " invalid\n"
		else:
			#if ISBN is not valid
			output = format(ISBNno, "<13") + " invalid\n"
		#write output to file	
		write_file.write(output)
	readfile.close()
	write_file.close()
main()




