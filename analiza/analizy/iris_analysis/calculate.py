from .io import load as l
from .io import save as s

def calculate():
    data = l.load()
    sep = data["sepal.length"]
    sepl = [sep.mean(), sep.median(), sep.std()]
    sepw = [data["sepal.width"].mean(), data["sepal.width"].median(), data["sepal.width"].std()]
    petl = [data["petal.length"].mean(), data["petal.length"].median(), data["petal.length"].std()]
    petw = [data["petal.width"].mean(), data["petal.width"].median(), data["petal.width"].std()]
    d = {"sepal length": sepl, 'sepal width':sepw, 'petal length':petl, "petal width":petw}

