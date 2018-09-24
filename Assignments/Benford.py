#  File: Benford.py

#  Description: Computing Benfords law on a text file of populaton statistics. 

#  Student Name: Naman Mehra

#  Student UT EID: nm26465

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:April 27th, 2017

#  Date Last Modified:April 29th, 2017

def main():
    pop_freq = {}

    pop_freq['1'] = 0
    pop_freq['2'] = 0
    pop_freq['3'] = 0
    pop_freq['4'] = 0
    pop_freq['5'] = 0
    pop_freq['6'] = 0
    pop_freq['7'] = 0
    pop_freq['8'] = 0
    pop_freq['9'] = 0

    lst_temp = [1,2,3,4,5,6,7,8,9]
    

    in_file = open("./census_2009.txt","r")

    header = in_file.readline()
    count = 0
    for line in in_file:
        count += 1
        line = line.strip()
        pop_data = line.split()
        pop_num = pop_data[-1]

        pop_num = int(pop_num)

        while pop_num > 0:
            temp = pop_num%10
            pop_num = pop_num//10

        for i in range(len(lst_temp)):
            if lst_temp[i] == temp:
                pop_freq[str(lst_temp[i])] = pop_freq[str(lst_temp[i])] + 1


    
    print("Digit   Count   %")
    for key in pop_freq:
        prob = 100*(int(pop_freq[key])/count)
        prob = round(prob, 1)

        print(format(str(key), "<8s"), end = '')
        print(format(str(pop_freq[key]), "<8s"), end = '')
        print(format(str(prob), "<8s"))
       
    
        
    in_file.close()
    
main()    





    
                
