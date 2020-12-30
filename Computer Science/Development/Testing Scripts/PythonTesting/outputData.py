import csv
    
def toCSV(fileInput):
    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(fileInput)