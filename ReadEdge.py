import csv

filename = 'EdgeIpSheet.csv'
Edge = []
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0:
            Edge.append(int(row[0]))
            pass
    c = Edge.index(1)
    pass
