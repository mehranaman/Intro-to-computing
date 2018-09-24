#  File: LinkedList.py
#  Description: Classes and methods for a given main code.
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: October 27th, 2017
#  Date Last Modified: October 27th, 2017



class Link(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class LinkedList(object):
        # String representation of data 10 items to a line, 2 spaces between data
	def __str__ (self):

		current = self.first
		ctr = 0
		string = ""

		while current.next != None:
			if ctr == 10:
				string += "\n"
				ctr = 0
			string += str(current.data) + "  "
			ctr += 1
			current = current.next

		if current.next == None:
			string += str(current.data) + "  "

		return string

	def __init__(self):
		self.first = None
		self.size = 0

	# get number of links
	def getLength(self):
		return self.size

	# Add data at the beginning of the linked list
	def addFirst(self, data):
		newLink = Link(data)
		newLink.next = self.first
		self.first = newLink
		self.size += 1

	# Add data at the end of a list
	def addLast (self, data): 
		self.size += 1
		newLink = Link(data)
		current = self.first
		if current == None:
			self.first = newLink
			return
		while current.next != None:
			current = current.next
		current.next = newLink

	# Add data in an ordered list in ascending order
	def addInOrder (self, data): 
		self.size += 1
		current = self.first
		previous = self.first
		newLink = Link(data)
		if current == None:
			self.first = newLink
			return
		if current!= None and ord(current.data[0])>ord(data[0]):
			self.addFirst(data)
			return 
		while current != None and current.data<=data:
			#print(current.data)
			previous = current
			current = current.next
		previous.next = newLink
		newLink.next = current
		return 



	# Search in an unordered list, return None if not found
	def findUnordered (self, data): 
		current = self.first

		if current == None:
			return False   ##

		while current.data != data:
			if current.next == None:
				return False####
			else:
				current = current.next

		return True

	# Search in an ordered list, return None if not found
	def findOrdered (self, data):
		current = self.first

		if current == None:
			return False

		while current.data != data:
			if current.next == None:
				return False    #####
			elif current.data > data:
				return False
			else:
				current = current.next

		return True

	# Delete and return Link from an unordered list or None if not found
	def delete (self, data):
		current = self.first
		previous = self.first

		if current == None:
			return None

		while current.data != data:
			if current.next == None:
				return None
			else:
				previous = current
				current = current.next

		if current == self.first:
			self.first = self.first.next
		else:
			previous.next = current.next

		return current.data

	


	#converts to list
	def convertList(self):
		current = self.first
		new_list = []
		while current.next != None:
			new_list.append(current.data)
			current = current.next
		if current.next == None:
			new_list.append(current.data)
		return new_list

	# Copy the contents of a list and return new list
	def copyList (self):
		current = self.first
		if current == None:
			return None
		new_Linklist = LinkedList()
		while current.next != None:
			new_Linklist.addLast(current.data)
			current = current.next
		if current.next == None:
			new_Linklist.addLast(current.data)
		return new_Linklist


	# Reverse the contents of a list and return new list
	def reverseList (self): 
		current = self.first
		if current == None:
			return None
		new_Linklist = LinkedList()
		while current.next != None:
			new_Linklist.addFirst(current.data)
			current = current.next
		if current.next == None:
			new_Linklist.addFirst(current.data)
		return new_Linklist


	# Sort the contents of a list in ascending order and return new list
	def orderList (self): 
		new_list = []
		new_Linklist = LinkedList()
		current = self.first
		if current == None:
			return None
		while (current.next != None):
			new_list.append(current.data)
			current = current.next
		if current.next == None:
			new_list.append(current.data)

		for item in new_list:
			new_Linklist.addInOrder(item)
		return new_Linklist

		

	# Return True if a list is sorted in ascending order or False otherwise
	def isOrdered (self):
		current = self.first

		if current == None:
			return None

		while current.next != None:
			if current.next == None:
				return None
			if ord(current.next.data[0]) <= ord(current.data[0]):
				return False
			else:
				current = current.next
				if current.next == None:
					return True

	# Return True if a list is empty or False otherwise
	def isEmpty (self): 
		return self.first == None

	# Merge two sorted lists and return new list in ascending order
	def mergeList (self, b): 
		new_Linklist = LinkedList()
		c = []
		a = self.convertList()
		a.sort()
		b = b.convertList()
		b.sort()
		idxA = 0
		idxB = 0
		while ((idxA < len(a)) and idxB < len(b)):
			if (a[idxA] < b[idxB]):
				c.append(a[idxA])
				idxA += 1
			else:
				c.append(b[idxB])
				idxB += 1
		while(idxA<len(a)):
			c.append(a[idxA])
			idxA += 1

		while (idxB<len(b)):
			c.append(b[idxB])
			idxB += 1

		#print(c)

		for item in c:
			new_Linklist.addLast(item)

		return new_Linklist
	
	


	def isEqual (self, b):
                
		a = self.convertList()
		b = b.convertList()
		
		return a == b
	# Return a new list, keeping only the first occurence of an element
	# and removing all duplicates. Do not change the order of the elements.
	def removeDuplicates (self):
		new_Linklist = LinkedList()
		newList = []
		copyList = self.convertList()
		for item in copyList:
			if item not in newList:
				newList.append(item)
		for item in newList:
			new_Linklist.addLast(item)
		return new_Linklist

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 
   
   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)
   
   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)
   
   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))
   
   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
