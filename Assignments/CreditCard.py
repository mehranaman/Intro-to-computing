#  File: CreditCard.py

#  Description: Code to categorize potential credit card numbers.

#  Student Name: Naman Mehra

#  Student UT EID: nm26465

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:April 7th, 2017

#  Date Last Modified: April 7th, 2017


def num_digits(card_number):
    #function used to accept the right number of digits.
    if ((card_number//(10**15) == 0) and (card_number//(10**14) > 0)) or (((card_number//(10**16)) == 0) and ((card_number//(10**15)) > 0)) :
        return 1
    else:
        return 0
                                                                          

def valid(card_number):
    #declaring variables used in the function.
    lst_odd = []
    lst_even = []
    sum_odd = 0
    sum_odd_digit = 0

    #making a copy just because don't want to play around with the original.
    card_number_copy = card_number
    if ((card_number//(10**15) == 0) and (card_number//(10**14) > 0)):
        int_number = 15
    else:
        int_number = 16

    if int_number == 15:
        for i in range (15):
            
            if i%2 == 0:
                digit = card_number_copy%10
                lst_even.append(digit)
                card_number_copy = card_number_copy//10

            if i%2 != 0:
                digit = card_number_copy%10
                lst_odd.append(digit)
                card_number_copy = card_number_copy//10

    else:
        for q in range(16):
            if q%2 == 0:
                digit = card_number_copy%10
                lst_even.append(digit)
                card_number_copy = card_number_copy//10

            if q%2 != 0:
                digit = card_number_copy%10
                lst_odd.append(digit)
                card_number_copy = card_number_copy//10
                

    for s in range(len(lst_odd)):
        sum_odd_digit = 0
        lst_odd[s] = 2*lst_odd[s]
        if lst_odd[s] >= 10:
                
            while lst_odd[s] > 0:
                
                sum_odd_digit = sum_odd_digit + lst_odd[s]%10
                lst_odd[s] = lst_odd[s]//10

            lst_odd[s] = sum_odd_digit

                
    sum_even = sum(lst_even)
    sum_odd = sum(lst_odd)                       

    total_sum = sum_odd + sum_even
    if total_sum%10 == 0:
        return 1
    else:
        return 0
         

def MII(card_number):
    
    if ((card_number//(10**15) == 0) and (card_number//(10**14) > 0)):
        
        if (card_number//(10**13)) == 34 or (card_number//(10**13)) == 37:
            print("Valid American Express credit card number")

        elif (card_number//(10**11)) == 6011 or (card_number//(10**12)) == 644 or (card_number//(10**13)) == 65:
            print("Valid Discover credit card number")

        elif (card_number//(10**13)) <= 55 and (card_number//(10**13)) >= 50:
            print("Valid MasterCard credit card number")

        elif (card_number//(10**14)) == 4:
            print("Valid Visa credit card number")
        else:
            print('valid credit card number')
    else:
        
        if ((card_number//(10**12)) == 6011) or ((card_number//(10**13)) == 644) or ((card_number//(10**14)) == 65):
            print("Valid discover credit card")
        
        elif (card_number//(10**14)) == 34 or (card_number//(10**14)) == 37:
            print("Valid American Express credit card number")


        elif (card_number//(10**14)) <= 55 and (card_number//(10**14)) >= 50:
            print("Valid MasterCard credit card number")

        elif (card_number//(10**15)) == 4:
            print("Valid Visa credit card number")
        else:
            print('Valid credit card number')       

    return


            
def main():
    card_number = int(input("Enter a 15 or 16-digit credit card number: "))
    
    if num_digits(card_number):
        
        if valid(card_number):
            
            MII(card_number)
            
        else:
            
            print("Invalid credit card number")
    else:
        print("Not a 15 or 16-digit number")
                
    
        
main()
            
            
                
            
           









    
