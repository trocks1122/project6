#Project 6
#Alex and Trevor

#Imports
import math
import random
import numpy as np
import csv
import sys
import re
import os.path
from node import Node

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
    #print ln
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
    #print ln2
    #create node
    bayNet.append(Node(ln2[0],ln2[2]))
    #check parent
    tempParent.append(ln2[1])

    #check for 2, 4, or 8 list
    #if len(ln[8:]) = 2:
        #set to probability
    #elif len(ln[8:]) = 4:
        #set to probability
    #elif len(ln[8:]) = 8:
        #set to probability   
fr.closed
#print bayNet
#print tempParent

 # set parent for node and go to parent node and set child node
for j in range(len(tempParent)):
    # check if node has parent
    tempP = tempParent[j]
    #print tempP
    tempN = bayNet[j]
    parentA = []
    if tempP:
        if len(tempP) == 2:
            tempP1 = tempP[0]
            tempP2 = tempP[1]
            #print tempP1
            #print tempP2
            for k in range(len(bayNet)):
               #print bayNet[k].name
               if bayNet[k].name == tempP1 or bayNet[k].name == tempP2: 
                   #Parent node found
                   #print "found parent"
                   bayNet[k].add_child(tempN)
                   parentA.append(bayNet[k])
                   #print len(parentA)
            #print parentA[0].name
            #print parentA[1].name
            bayNet[j].add_parent(parentA[0])
            bayNet[j].add_parent(parentA[1])
        if len(tempP) == 1:
            tempP1 = tempP[0]
            if tempP1 != '':
                for k in range(len(bayNet)):
                    if bayNet[k].name == tempP1: 
                        #Parent node found
                        bayNet[k].add_child(tempN)
                        parentA.append(bayNet[k])
                bayNet[j].add_parent(parentA[0])

#Test node
print "Beginning Test of Setup"
for l in range(len(bayNet)):
    #print bayNet[l]
    #print bayNet[l].name
    bayNet[l].print_node()

#Take in second script
print "Take in query..."
fs = open(inputQ)
lines2 = fs.readlines()
query = lines2[0].rstrip('\n')
query = query.split(',')
fs.closed
print query
for m in range(len(bayNet)):
    bayNet[m].setQuery(query[m])

#run querry
print "Run querry..."

#rejection sampling
def rejection sampling:
    print "Begin Rejection Sampling..."
    
    #find querry value
    #check for parents
    #return probabilty


#Likelyhood-weighing
def likeWeigh:
    print "Begin likelyhood Weighing..."
    #assume ecidence is true, then add weight to nodes



