import csv

# Fetch the csv to fetch the id for the states of the country
with open('./lgas.csv', 'r') as lga1:
    reader = csv.reader(lga1)
    header = next(reader)
    data = [[item.strip() for item in row] for row in reader]

    with open('./sth.csv', 'w') as lga2:
        writer = csv.writer(lga2)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)