import csv
import copy

my_vehicle = {
    "vin": "<empty>",
    "make": "<>empty",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "top_speed": 0,
    "zero_sixty": 0.0,
    "mileage": 0
}

for key, value in my_vehicle.items():
    print(f'{key}: {value}')

# Define an empty list to hold the car inventory that you will read
my_inventory_list = []


with open('car_fleet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    linecount = 0
    for row in csv_reader:
        if linecount == 0:
            print(f'Column names are: {", ".join(row)}')
            linecount += 1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, top_speed: {row[5]}, zero_sixty{row[6]}, mileage: {row[7]}' )
            current_vehicle = copy.deepcopy(my_vehicle)
            current_vehicle["vin"] = row[0]
            current_vehicle["make"] = row[1]
            current_vehicle["model"] = row[2]
            current_vehicle["year"] = row[3]
            current_vehicle["range"] = row[4]
            current_vehicle["top_speed"] = row[5]
            current_vehicle["zero_sixty"] = row[6]
            current_vehicle["mileage"] = row[7]
            my_inventory_list.append(current_vehicle)
            linecount += 1
    print(f'Processed {linecount} lines.')
    
    
    # Printing the car inventory
    for my_car_properties in my_inventory_list:
        for key, value in my_car_properties.items():
            print(f'{key}: {value}')
            print("-----")