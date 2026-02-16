import csv

def read_names_from_csv(filepath):
    names = []
    with open(filepath, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row[0])
    return names
