#  File: Intervals.py

#  Description: Collapsing intervals

#  Student Name: Naman Mehra 

#  Student UT EID: nm26465

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:April 25th, 2017

#  Date Last Modified:April 25th, 2017


def main():
    

 
    in_file = open('intervals.txt', 'r')

    interval = []

    for line in in_file:
      # Stripping white spaces and convert str to int
        line = line.strip().split()

        line[0] = int(line[0])
        line[1] = int(line[1])
        element = tuple(line)
        interval.append(element)

  
    interval.sort()

    
    
    for i in range(len(interval)):
        while i < len(interval)-1:
            if interval[i+1][0] <= interval[i][1]:
                interval[i] = (interval[i][0], max(interval[i][1], interval[i+1][1]))

                del interval[i+1]

            else:
                break

    
    
    
    interval.sort()
    print("Non-intersecting Intervals: ")
    for i in range(len(interval)):
        print(interval[i])
   
        
    
    interval_new = []
    for i in range(len(interval)):
        interval_new.append((interval[i][1]-interval[i][0] , i))

    interval_new.sort()

    
    new_list = []
    for i in range(len(interval_new)):
        new_list.append(interval[interval_new[i][1]])

    print("Non-intersecting Intervals in orer of size: ")
    for j in range(len(new_list)):
        print(new_list[j])

    
            
                   
    in_file.close()





main()



