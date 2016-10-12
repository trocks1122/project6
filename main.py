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
import random
import networkx as nx
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

def past_sample(dist):
    #returns sample from past distribution
    t = dist#[dist[s] for s in nx.topological_sort(dist)]
    assigns = {}

    j = 0
    for node in t:
        rand = random.uniform(0,1)
        parent_prob = rand
        if len(node.parents) > 0: #probability given parents
            parent_prob = prob_if_parents(node, assigns)
        else:  #given no parents
            parent_prob = node.cpt[0]

        assigns[node.name] = True if rand < parent_prob else False
        j += 1
    return assigns


def weighted(dist, e):
    t = dist#.node[s]['obj'] for s in nx.topological_sort(dist)]
    assigns = {}
    x = 0  
    weight = 1

    for node in t:
        rand = random.uniform(0,1)
        parent_prob = rand
        int(parent_prob)
        int(weight)

        if len(node.parents) > 0: #probability given parents
            parent_prob = prob_if_parents(node, assigns)
        else:  #given no parents
            parent_prob = node.cpt[0]
        if node.name in e:
            weight *= (1 - parent_prob) if e[node.name] is False else parent_prob
        else:
            assigns[node.name] = True if rand < parent_prob else False
        x += 0 
    return assigns, weight




        
def prob_if_parents(node, assigns):
    parent_names = [n.name for n in node.parents]
    parent_prob = [assigns[p] for p in parent_names if p in assigns]
    row = node.cpt
    for r in range(len(node.cpt)):    
        is_match = True
        for j in xrange(0, len(parent_prob)):
            if row[r] != parent_prob[j]:
                is_match = False
        if is_match:
            p = row[-1]

    return p


def consistent(x, e):
    Consistent = True
    for num in x:
        if num in e and x[num] != e[num]:
            consistent = False
    return Consistent


def normalize(norm):
    return {h: float(v) / sum(norm.values()) for h, v in norm.iteritems()} if sum(norm.values()) > 0 else None


def get_query_evidence(bn):
    """
    Takes in a network and returns a dictionary of the query variable
    + evidence nodes, mapping their names to their values
    (i.e. {X: <query_var>, e: {<evid_var>: <evid_value})
    """
    a = {}
    e = {}
    for n in range(len(bn)):
        node = bn[n]
        if node.queryV == 1:
            e[node.name] = True
        elif node.queryV == 0:
            e[node.name] = False
        elif node.queryV == 2:
            a['X'] = node.name
        a['e'] = e
    return a


#rejection sampling
def rejection_sampling(x, e, b, count):
    print "Begin Rejection Sampling..."
    
    n = {True: 0, False: 0}

    for i in xrange(0, count):

        ls = past_sample(b)

        if consistent(ls, e):
            h = ls[x]
            n[h] += 1
    return normalize(n)

qe = get_query_evidence(bayNet)
print rejection_sampling(qe['X'], qe['e'],bayNet,int(inputA))


#Likelyhood-weighing
def likeWeigh(x, e, b, count):
    print "Begin likelyhood Weighing..."
    n = {True: 0, False: 0}

    for i in xrange(0, count):
        y, weight = weighted(b, e)
        
        num = y[x]
        n[num] += weight

    return normalize(n)

print likeWeigh(qe['X'], qe['e'],bayNet,int(inputA))


    #assume ecidence is true, then add weight to nodes



