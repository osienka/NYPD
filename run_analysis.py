from iris_analysis import calculate as c
from iris_analysis.io import load as l
from iris_analysis.io import save as s
import sys

def main():
    s.save(c.calculate(l.load(sys.argv[1])), sys.argv[2])

main()
