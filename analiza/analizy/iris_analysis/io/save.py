import csv

def save(data, fileDir: str):
    with open(fileDir, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return writer
