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

tempP = []
bayNet = []
tempParent = [] #array holds parents for each node to set to later
fr = open(inputBN) 
lines = fr.readlines()

for i in range(len(lines)):
    
    #rearrange input into data
    ln = lines[i].rstrip('\n')
    print ln
    ln1 = ln.split(': ')
    ln1a = ln1[1].split('] [')
    ln2 = []
    ln2.append(ln1[0])
    ln2.append(ln1a[0])
    ln2.append(ln1a[1])
    ln2[1] = ln2[1].replace('[','')
    ln2[1] = ln2[1].split(' ')
    ln2[2] = ln2[2].replace(']','')
    ln2[2] = ln2[2].split(' ')
    temp1 = []
    temp2 = ln2[2]
    for j in range(len(temp2)):
        temp1.append(float(temp2[j]))
    ln2[2] = temp1
    print ln2
    #create node
    



    #check parent
    #tempParent.append(2)

    #check for 2, 4, or 8 list
    #if len(ln[8:]) = 2:
        #set to probability
    #elif len(ln[8:]) = 4:
        #set to probability
    #elif len(ln[8:]) = 8:
        #set to probability   
fr.closed

#for j in range(len(tempParent)):
    # check if node has parent
    # set parent for node and go to parent node and set child node

#Take in second script
print "Take in query"
fs = open(inputQ)
lines2 = fs.readlines()
querry = lines2[0].rstrip('\n')
querry = querry.split(',')
print querry

#run querry



