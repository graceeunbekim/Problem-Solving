# Grace Eunbe Kim
# contact: eunbegracekim40@gmail.com

# Zillow question 2
# Implement insert and delete in a tri-nary tree. A tri-nary tree is much like a binary
# tree but with three child nodes for each parent instead of two -- with the left node being values 
# less than the parent, the right node values greater than the parent, and the middle nodes values 
# equal to the parent.
class Node:
	def __init__(self, value):
		"""
		Node class has four instances to assign a left, mid, and right children
		of a node. isRoot determines if a node is root or not. Value indicates an
		integer number of a node.
		"""
		self.left_child  = None
		self.mid_child   = None
		self.right_child = None
		self.value = value

	def getLeftChild(self):
		"""getLeftChild returns a value of a left child of current node."""
		return self.left_child.value

	def getMidChild(self):
		"""getMidChild returns a value of a middle child of current node."""
		return self.mid_child.value

	def getRightChild(self):
		"""getRightChild returns a value of a right child of current node."""
		return self.right_child.value

class TriSearchTree:
	"""
	A tri-nary tree is much like a binary tree but with three child nodes 
	for each parent instead of two -- with the left node being values less than the parent, 
	the right node values greater than the parent, and the middle nodes values equal to the parent. 
	"""
	def __init__(self):
		self.root = None

	def insertNode(self, value):
		"""insertNode insert a node to a tree. Left node being value less than the parent,
		the right node values greater than the parent, and the middle nodes values equal
		to the parent."""
		if (self.root == None):
			self.root == Node(value)

		else:
			current = self.root

			if (value < current.value):
				if (current.left_child):
					current = current.left_child

				else:
					current.left_child = Node(value)

			elif (value == current.value):
				if (current.mid_child):
					current = current.mid_child

				else:
					current.mid_child = Node(value)

			else:
				if (current.right_child):
					current = current.right_child
				else:
					current.right_child = Node(value)

	def printTreeInOrder(self, node):
		"""printTreeInOrder prints a tree data structure in order."""
		print "heyyy"
		if (node is not None):
			self.printTreeInOrder(node.left_child)
			print node.value
			self.printTreeInOrder(node.mid_child)
			print node.value
			self.printTreeInOrder(node.right_child)


def main():
	"""main method of the class. Inserts values into a tree, and prints the
	tree in order."""
	triTree = TriSearchTree()

	triTree.root = triTree.insertNode(5)

	triTree.insertNode(4)
	triTree.insertNode(9)
	triTree.insertNode(5)
	triTree.insertNode(7)
	triTree.insertNode(2)
	triTree.insertNode(2)
	triTree.printTreeInOrder(triTree.root)


main()

