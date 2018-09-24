#  File: ERsim.py
#  Description: Emergency room services simulation
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: October 19th, 2017
#  Date Last Modified: October 19th, 2017



class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []


    def __str__(self):
        print (self.items)

        
#creating functions for specific commands


def treat(critical, serious, fair):

    
    
    if critical.isEmpty() == False:

        #printing queues for each class
        
        print("Treating: ", critical.items[-1], "from Critical.")
        critical.dequeue()
        print("Queues are: ")
        print("Fair: ",fair.items)
        print("Serious: ", serious.items)
        print("Critical: ", critical.items)
        return

    elif serious.isEmpty() == False:
        print("Treating ", serious.items[-1], "from serious.")
        serious.dequeue()
        print("Queues are: ")
        print("Fair: ",fair.items)
        print("Serious: ", serious.items)
        print("Critical: ", critical.items)
        return

    elif fair.isEmpty() == False:
        print("Treating ", fair.items[-1], " from fair.")
        fair.dequeue()
        print("Queues are: ")
        print("Fair: ",fair.items)
        print("Serious: ", serious.items)
        print("Critical: ", critical.items)
        return

    else:
        print("No patients in queues.")
        return

    

def main():
 
    #creating queue lists for each case.
    critical = Queue()
    serious = Queue()
    fair = Queue()


    # creating and reading file, storing as a string.
    file = open("ERsim.txt" , "r")


    #reading each line individually
    
    for line in file:

        
        line = line.rstrip(' ')
        

        if line[0:3] == 'add':
            
            #handling variety of commands
            
            
            if line[4:12] == 'Critical':
                critical.enqueue(line[13:-1])
                print('\n\nCommand: ', line[:-1])
                print("Queues are: ")
                print("Fair: ",fair.items)
                print("Serious: ", serious.items)
                print("Critical: ", critical.items)

            if line[4:11] == 'Serious':  #serious condition
                serious.enqueue(line[12:-1])
                print('\n\nCommand: ', line[:-1])

                
                print("Queues are: ")
                print("Fair: ",fair.items)
                print("Serious: ", serious.items)
                print("Critical: ", critical.items)

            if line[4:8] == 'Fair':
                fair.enqueue(line[9:-1])
                print('\n\nCommand: ', line[:-1])

                
                print("Queues are: ")
                print("Fair: ",fair.items)
                print("Serious: ", serious.items)
                print("Critical: ", critical.items)
            


        if line[0:7] == 'treat n':  #treat next
            print("\n\nCommand: Treat next.")
            treat(critical, serious, fair)
                

            
        if line[0:7] == 'treat C':    #treat critical
            print("\n\nCommand:  Treat next patient in critical queue.")

            if len(critical.items) > 0:   
                print("Treating ", critical[-1], "from critical queue.")

                critical.dequeue()                    
    
                print("Queues are: ")
                print("Fair: ",fair.items)
                print("Serious: ", serious.items)
                print("Critical: ", critical.items)
                    

            else:
                print("No patient in critical queue.")
                
                
        if line[0:7] == 'treat S':    #treat serious
            print("\n\nCommand:  Treat next patient in serious queue.")

            if len(serious.items) > 0:
                print("Treating ", serious.items[-1], " from serious queue.")

                serious.dequeue()                    
    
                print("Queues are: ")
                print("Fair: ",fair.items)
                print("Serious: ", serious.items)
                print("Critical: ", critical.items)
                    

            else:
                print("No patient in serious queue.")
                
                
        if line[0:7] == 'treat F':   #treat Fair
            print("\n\nCommand:  Treat next patient in fair queue.")

            if len(fair.items) > 0:
                print("Treating ", fair.items[-1], " from fair queue.")

                fair.dequeue()                    
    
                print("Queues are: ")
                print("Fair: ",fair.items)
                print("Serious: ", serious.items)
                print("Critical: ", critical.items)
                    

            else:
                print("No patient in critical queue.")

        if line[0:7] == 'treat a':    #treal all
            
            print("\n\nCommand: Treat all patients: ") 
            while (critical.isEmpty() == False) or (serious.isEmpty() == False)or (fair.isEmpty() == False):
                print("\n")
                treat(critical, serious,fair)

            print("No patients in queues.")

        if line[0:4] == 'exit':   #exit
            return

        
main()
                

                
            


















        



