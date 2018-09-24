#  File: htmlChecker.py
#  Description: This program checks if html tags are correctly matched
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created:10/13/17
#  Date Last Modified:10/13/17


#copy-paste list implementation of stack
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def size(self):
        return(len(self.items))
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return(self.items[-1])

    def __str__ (self):
        return str(self.items)

def getTag(file):
  #read all the lines of the file
  infile=open(file,"r")
  lines=infile.readlines()
  #initialize taglist
  taglist=[]
  
  flag=False
  #go through lines
  for line in lines:
    str=""
    line=line.strip()
    #go through each character
    for char in line:
      #append characters between "<" and ">"
      if char!=">" and flag:
        
        str=str+char
      if char=="<":
        flag=True
        str=""  
        
      if char==">":
        flag=False
        taglist.append(str) 
    if str=="":
      continue
         
    

  
  return(taglist)


    
  

def main():
  #initialize stack
  s=Stack()

  #call getTag function
  taglist=getTag("htmlfile.txt")
  print(taglist)
  print()
  flag=True
  index=0
  validtags=[]
  #create list of exceptions
  exceptions=['br','hr','meta http-equiv="content-type" content="text/html; charset=windows-1252"']

  #iterate through taglist
  while index < len(taglist) and flag:

    #isolate the tag
    string=str(taglist[index])
    #check if the tag is an exception
    if string in exceptions:
      print("Tag",string,"does not need a match: stack is still",s)
    #check if tag is end tag
    elif string[0]=="/" :
      topvalue=s.peek()
      
      match=string[1:]
      #check if endtagmatches
      if match==topvalue:
        #pop start tag that matches the end tag
        s.pop()
        
        print("Tag",string,"matches top of stack:  stack is now",s)

        #check if tag is already in validtags
        if string[1:] in validtags:
          pass
        else:
          #append tag to validtags 
          validtags.append(string[1:])
          print("New tag",string,"found and added to list of valid tags.")
        
      #if tag does not match,show error
      else:
        print("Error: tag is",string,"top of stack is",s.peek())
        break
    
    #check if tag is a start tag
    elif string[0]!="/":
      #push start tag to stack
      s.push(string)
      print("Tag",string,"pushed: stack is now",s)
    index=index+1

  #check if list is empty or not
  if s.isEmpty():
    print("Processing complete. No mismatches found.")
  elif s.isEmpty()=="False":
    print("Processing complete. Unmatched tags remain on stack: ",s)
  print()
  print()
  print("Valid tags are:",sorted(validtags))
  print("Exceptions are:",sorted(exceptions))
  
      
      
      


    

  
main()
   
    
      
    
  
      
  
        
        

    
    
