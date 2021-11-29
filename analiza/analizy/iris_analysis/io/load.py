import sys
import csv

def load():
    d = {}
    with open(sys.argv[1], newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for j in spamreader[0]:
            d.keys.append(j)
        for row in range(1,len(spamreader)):
            for i in range(len(row)):
                d[i].append(spamreader[i])
    return d
