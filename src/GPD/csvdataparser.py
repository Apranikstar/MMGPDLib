import csv

def get_flavour_values(dataFilename, flavourKeyList):
    result = {}

    with open(dataFilename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            flavour = row[0]
            if flavour in flavourKeyList:
                result[flavour] = [eval(value) for value in row[1:]]
    return result

