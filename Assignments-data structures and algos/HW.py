#  File: Dice.py
#  Description: Dice game simulation
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: November 7th, 2017
#  Date Last Modified: November 10th, 2017


class User(object):

    def __init__(self, name):
        self.name = name
        self.next = None
        self.next_list_friend = None
        

    def setNext(self, newNext):
        self.next = newNext

    def setNextfriend(self, newNextfriend):
        self.next_list_friend = newNextfriend

    def getNext(self):
        return self.next

    def getNextfriend(self):
        return self.next_list_friend
        

    def getName(self):
        return self.name

    def addFriend(self, friend):
        tempf = friend
        
        tempf.setNextfriend(self.getNextfriend())
        self.setNextfriend(tempf)
    
        
        
        

class UnorderedList(object):

    people = []
    
    def __init__(self):
        self.head = None
       

    def add (self, item):
        item.setNext(self.head)
        self.head = item


    
    def exist(self, member):
        current = self.head
        found = False
        while current != None and found == False:
            if current.getName() != member:
                current = current.getNext()
            else:
                found = True
        return found

    def find(self, name):
        current = self.head
        found = False
        while current != none and found == False:
            if current.name != member:
                current = current.getNext()
            else:
                found = True
        return 
        
        
    def find_n_add(self, name1, name2):
        current = self.head
        found = False
                    
        while current != None and current.getName() != name1:
            
            current = current.getNext()
        
        temp = User(name2)
        current.addFriend(temp)
        
        
    def find_friend(self, name1, name2):
        current = self.head
        found  = False
        while current != None and found == False:
            if current.getName() == name1:
                found = True

            else:

                current = current.getNext()
        if current == None:
            print(name1, " doesn't have an account.")
            return
        if found == True:
            switch = False
            current = current.getNextfriend()
            while switch == False and current != None:
                if current.name == name2:
                    switch = True
                else:
                    current = current.getNextfriend()
        return switch

    def list_friends(self, name):
        current = self.head
        
        found = False
        
        while found == False:
            
            if current.getName() == name:
                found = True
            else:    
                current = current.getNext()

        current = current.getNextfriend()
        if current == None:
            print(name, " has no friends.")
        else:
            print('[', end= ' ')
            while current != None:
                print(current.getName(), end = ' ')
                current = current.getNextfriend()
            print(']')
        

    def unfriend(self, name1, name2):
        current = self.head
        found  = False
        while current.getName() != name1 and found == False:
            if current.name == name1:
                found = True

            else:
                current = current.getNext()
        
        switch = False
        previous = None

        while current != None and switch == False:
            if current.getName() != name2:
                previous = current
                current = current.getNextfriend()
            else:
                switch = True

        previous.setNextfriend(current.getNextfriend())
        


    
def main():


    
    member_list = UnorderedList()
    people = []

    #reading the file
    file = open("FriendData.txt", "r")

    for line in file:
        
        line = line.rstrip(' ')
        
        split_line = line.split()

        print()
        print("-->", line, end = '    ')
        


        if line[0] == 'P':
            
            if not member_list.exist(split_line[1]):
                newmember = User(split_line[1])
                member_list.add(newmember)
                print(split_line[1] ," now has an account.")

                
            else:
                print("A member by this name already exists.")

        if line[0] == 'F':
            if split_line[1] != split_line[2]:
                if not member_list.exist(split_line[1]):
                    if not member_list.exist(split_line[2]):
                        print("Both members don't exist.")
                    else:   
                        print(split_line[1], " doesn't have an account.")

                else:
                    if not member_list.exist(split_line[2]):
                        print(split_line[2], " doesn't have an account.")
                    else:
                        if not member_list.find_friend(split_line[1], split_line[2]):
                            member_list.find_n_add(split_line[1], split_line[2])
                            member_list.find_n_add(split_line[2], split_line[1])
                            print(split_line[1], " and ", split_line[2], " are now friends.")
                        else:
                            print(split_line[1], " and ", split_line[2] ," are already friends.")
            else:
                print("A person can't add himself/herself.")
        if line[0] == 'U':
            if split_line[1] != split_line[2]:
                if not member_list.exist(split_line[1]):
                    if not member_list.exist(split_line[2]):
                        print("Both members don't exist.")
                    else:
                        print(split_line[1], "doesn't have an account.")
                else:
                    if not member_list.exist(split_line[2]):
                        print(split_line[2], "doesn't have an account.")

                    else:
                        if not member_list.find_friend(split_line[1], split_line[2]):
                            print("This friendship doesn't exist.")

                        else:
                            member_list.unfriend(split_line[1], split_line[2])
                            member_list.unfriend(split_line[2], split_line[1])
                            print(split_line[1], "and", split_line[2], "are no longer friends.")
                    
                
                    

            else:
                print("A person can't unfriend himself/herself.")
                
                
                
            
        if line[0] == 'Q':
            if split_line[1] == split_line[2]:
                print("A person can't query himself/herself.")

            else:
                
                if not member_list.exist(split_line[1]):
                    print(split_line[1],"doesn't have an account")
                else:
                    if not member_list.exist(split_line[2]):
                        print(split_line[2],"doesn't have an account.")

                    else:
                        if member_list.find_friend(split_line[1], split_line[2]):
                            print(split_line[1], " and ", split_line[2], " are friends.")
                        else:
                            print(split_line[1], " and ", split_line[2] , " are not friends.")

        if line[0]  == 'L':
            if member_list.exist(split_line[1]):
                
                member_list.list_friends(split_line[1])
            else:
                print(split_line[1], " doesn't have an account.")
            

        
                
        if line[0] == 'E':
            print("Exiting..")
            file.close()
            return



                

            
main()
                    
            
                
                

            
                







                      
                      
                      
                
                
           
            



            
