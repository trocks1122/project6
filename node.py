##project 6
##Trevor Rocks
##Alex Ruggiero



#globals
NODE_FALSE = 0
NODE_TRUE = 1
IS_QUERY = 2
UNKOWN = 4


class Node(object):

	"""docstring for Node"node
	def __init__(self, arg):
		super(Node,node).__init__()
		self.arg = arg"""
		

	name = ""
	parents = [] #if we do option A make length 2
	children = []
	cpt = []

	def add_parent(self, parent):
		if len(parents) < 2:
			parents.append(parent)
		else:
			print "only 2 parents allowed"


	def add_child(self, child):
		children.append(child)

	def set_cpt(self, new_cpt):
		cpt = new_cpt

	def probGivenParent(self, given_parents):
		index = 0

		for node in given_parents:
			parent_index = self.parents.index(n)
			index = index ^ (1 << parent_index)

		return cpt[index]

	    def print_node(node):
        print "Name: " + name
        print "Parents" + node.parents[0] + node.parents[1]


class Tree(object):
    #a tree is a list of parents and their children and their children ect

