#!/usr/bin/env python
"""mapper.py"""

import sys

#processing inputData
def inputPoints():
    datalist = []
    dataset = open('new_dataset_1.txt', 'r')
    for line in dataset:
        datalist.append(line)
    inputData = {}
    for data in datalist:
        gene = data.split('\t')
        attributes = []
        for i in range(2,len(gene)):
            if i == len(gene)-1:
                gene[i] = gene[i].split('\n')[0]
            attributes.append(gene[i])
        inputData[gene[0]] = attributes 
    return inputData

def Euclideandistance(first,second):

    x = tuple([float(p) for p in first])
    y = tuple([float(m) for m in second])
    dist = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return dist

# get the datapoint and centroids and calculate minimumdistance and assign it to the nearest cluster
inputPoint = inputPoints()
for features in inputPoint:
        distance = []
        for line in sys.stdin:
            line = line.strip()
            points = line.split()
            centre = []
            for x in range(0,len(points)):
                if x != 0:
                    centre.append(points[x])
            firstpoint = inputPoint.get(features)
            first = [float(q) for q in firstpoint]
            secondpoint = centre
            distance.append(Euclideandistance(firstpoint,secondpoint))
        mindist = min(distance)
        i = distance.index(mindist)
        #pass(cluster_id,gene_id,gene_attributes) to the reducer
        print(str(i)+"\t"+features+"\t"+str(first))