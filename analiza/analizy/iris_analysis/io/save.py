import sys
import csv
def save(data):
    with open(sys.argv[2], 'w') as writer:
        for i in range(len(data)):
            for j in range(len(i)):
                writer.write(data[i][j])
                writer.write(',')
            writer.write(' ')
    return writer
