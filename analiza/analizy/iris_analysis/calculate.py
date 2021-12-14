import statistics

def calculate(data):
    sepL = [item[0] for item in data]
    sepW = [item[1] for item in data]
    petL = [item[2] for item in data]
    petW = [item[3] for item in data]
    sepl = ['sepal length', statistics.mean(sepL), statistics.median(sepL), statistics.stdev(sepL)]
    sepw = ['sepal width', statistics.mean(sepW), statistics.median(sepW), statistics.stdev(sepW)]
    petl = ['petal length', statistics.mean(petL), statistics.median(petL), statistics.stdev(petL)]
    petw = ['petal width', statistics.mean(petW), statistics.median(petW), statistics.stdev(petW)]
    header = ['name', 'mean', 'median', 'std']
    d = [header, sepl, sepw, petl, petw]
    return d
