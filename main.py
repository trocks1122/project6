#Project 6
#Alex and Trevor

#Imports
import math
import random
import numpy as np
import csv
import sys
import re

#from StringIO import StringIO


#arguements from input  file
script, inputBN, inputQ, inputA = sys.argv

#Setup Bay Net
print "Setting up Bay Net..."
bayNet = []
tempParent = [] #array holds parents for each node to set to later
fr = open(input) 
lines = fr.readlines()

for i in range(len(lines)):
    ln = lines[i].rstrip('\n')
    print ln
    #create new node
    
    #check parent
    tempParent.append(2)

    #check for 2, 4, or 8 list
    if len(ln[8:]) = 2:
        #set to probability
    elif len(ln[8:]) = 4:
        #set to probability
    elif len(ln[8:]) = 8:
        #set to probability   


for j in range(len(tempParent)):
    # check if node has parent
    # set parent for node and go to parent node and set child node

