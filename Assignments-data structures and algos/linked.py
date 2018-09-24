


class Link(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class LinkedList(object):
    
    def __str__ (self):

        current = self.first
        ctr = 0
        string = ''

        while current != None:
            if ctr == 10:
                string += '\n'
                ctr = 0

            string += str(current.data) + '  '
            ctr += 1
            current = current.next

            if current.next == None:
                string += string(current.data) + '  '

            return string


    def __init__ (self):
        self.first == None
        self.size == 0

    def addFirst(self,item):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink
        self.size += 1

    def addLast(self,item):
        newLink = Linnk(data)
        current = self.first

        if current == None:
            self.first = newLink
            return
        while current.next != None:
            current = current.next
        current.next = newLink

    def addInOrder(self,data):
    
        
        current = self.first
        previous = self.first
        newLink = Link(data)
        if current == None:
            self.first = newLink
            return
        if current != None 
        
            





