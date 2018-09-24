#  File: MultiwayTreesInput
#  Description: Trees and children
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51915
#  Date Created: 12/8/2017
#  Date Last Modified: 12/8/2017


class MultiwayTree:
	
	# initialize
	def __init__(self, pyTree):
		
		self.data = pyTree[0]
		self.children = []
		
		for child in pyTree[1]:
			childTree = MultiwayTree(child)
			self.children.append(childTree)
	
	# print out the tree in pre-order fashion
	def preOrder(self):
		st = str(self.data) + " "
		if len(self.children) > 0:
			for child in self.children:
				st += child.preOrder()
		return st
			
	
	
	def isIsomorphicTo(self, other):
		isIsomorphic = True
		
		# check if the lengths of the children is the same
		if len(self.children) != len(other.children):
			return False
		
		# checking isomorphism for each child
		if len(self.children) > 0:
			for i in range(len(self.children)):
				isIsomorphic = self.children[i].isIsomorphicTo(other.children[i])
		
		return isIsomorphic

def main():
	
	infile = open("MultiwayTreeInput.txt", "r")
	
	
	unformatedTrees = []
	for line in infile:
		unformatedTrees.append(eval(line))
	infile.close()
	
	for i in range(0, len(unformatedTrees), 2):
		firstTree = unformatedTrees[i]
		secondTree = unformatedTrees[i+1]
		
		print()
		
		#printing trees, converting to multiway and then preorder
		print("Tree %d:" % (i+1), firstTree); firstTree = MultiwayTree(firstTree)
		print("Tree %d preorder:" % (i+1), firstTree.preOrder())
		
		print()
		
		print("Tree %d:" % (i+2), secondTree); secondTree = MultiwayTree(secondTree)
		print("Tree %d preorder:" % (i+2), secondTree.preOrder())
		
		print()
		
		#check if trees are isomorphic
		if firstTree.isIsomorphicTo(secondTree):
			print("Tree %d is isomorphic to Tree %d" % (i+1, i+2))
		else:
			print("Tree %d is not isomorphic to Tree %d" % (i+1, i+2))
		
		print()
	
main()
