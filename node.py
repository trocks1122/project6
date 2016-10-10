##project 6
##Trevor Rocks
##Alex Ruggiero
import math



#globals
NODE_FALSE = 0
NODE_TRUE = 1
IS_QUERY = 2
UNKNOWN = 4


class Node(object):
    """docstring for Node"node
    def __init__(self, arg):
        super(Node,node).__init__()
        self.arg = arg"""
    #name = ""
    #parents = [] #if we do option A make length 2
    #children = []
    #cpt = []

    def __init__(self, name, probability):
        self.name = name
        self.parents = []
        self.children = []
        self.cpt = probability
        self.queryV = UNKNOWN	

    def add_parent(self, parent):
        self.parents.append(parent)
        #print parent

    def add_child(self, child):
        self.children.append(child)
        #print child

    #def set_cpt(self, new_cpt):
    #    cpt = new_cpt

    def probGivenParent(self, given_parents):
        index = 0
        for node in given_parents:
            parent_index = self.parents.index(n)
            index = index ^ (1 << parent_index)
        return cpt[index]
    
    def setQuery(self, query):
        if query == '?' or query == 'q':
            self.queryV = IS_QUERY
        if query == '-':
            self.queryV = UNKNOWN
        if query == 'f':
            self.queryV = NODE_FALSE
        if query == 't':
            self.queryV = NODE_TRUE

    def print_node(self):
        print "Node==============="
        print "Name: " + self.name
        print "Parents: " 
        if not self.parents:
            print "None"
        else: 
            tempP = self.parents
            if len(tempP) == 1:
                tempP1 = tempP[0]
                print tempP1.name
            elif len(tempP) == 2:
                tempP1 = tempP[0]
                tempP2 = tempP[1]
                print tempP1.name
                print tempP2.name


#class Tree(object):
    #a tree is a list of parents and their children and their children ect

