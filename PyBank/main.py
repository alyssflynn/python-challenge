import os
import csv 

budget_data_1 = ("raw_data", "budget_data_1.csv")
budget_data_2 = ("raw_data", "budget_data_2.csv")

# Open budget_data_1.csv
with open(budget_data_1) as budget1:
    csvreader = csv.reader(budget1, delimiter=",")

    # Skip first row
    next(csvreader)


# Open budget_data_2.csv
with open(budget_data_2) as budget2:
    csvreader2 = csv.reader(budget2, delimiter=",")


def main():
    print("Nothin to see here folks")

if __name__ == "__main__":
    main()