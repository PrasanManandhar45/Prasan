'Program to read records.csv and display student details'''

import csv

try:
    with open("records.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print("Name:", row[0])
            print("Roll No:", row[1])
            print("Program:", row[2])
            print("Year:", row[3])
            print("Group:", row[4])
            print("----------------------")

except FileNotFoundError:
    print("File not found!")