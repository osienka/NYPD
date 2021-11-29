import csv

def load(fileDir: str):
    d = []
    with open(fileDir, encoding="utf8") as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            d.append(line)
        for i in range(1, len(d)):
          for j in range(4):
                d[i][j] = float(d[i][j])
    return d[1:]
