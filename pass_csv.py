import csv

# Fetch the csv to fetch the id for the states of the country
with open('./states.csv', 'r') as state_file:
    reader1 = csv.reader(state_file)
    header1 = next(reader1)
    data1 = [[item.strip() for item in row] for row in reader1]

    with open('./lgas.csv', 'r') as lga_file:
        reader2 = csv.reader(lga_file)
        header2 = next(reader2)
        data2 = [[obj.strip() for obj in field] for field in reader2]
        
        a = header1.index('name')
        b = header2.index('State')

        with open('output.csv', 'w') as output_file:
            header2.append('state_id/id')
            writer = csv.writer(output_file)
            writer.writerow(header2)
            
            for row in data2:
                for field in data1:
                    if row[b].lower() == field[a].lower():
                        row.append('__export__.res_country_state_' + str(field[header1.index('id')]))

                writer.writerow(row)