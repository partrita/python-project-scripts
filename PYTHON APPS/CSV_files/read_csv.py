import csv

import pandas as pd


def read_using_DictReader(path):
    # opening the CSV file
    with open(path, mode='r') as file:
        # reading the CSV file
        csvFile = csv.DictReader(file)
        return list(csvFile)


# return the top 5 rows in CSV file
def read_by_pandas_head(path):
    data = pd.read_csv(path)
    return data.head()


# return the bottom 5 rows in CSV file
def read_by_pandas_tail(path):
    data = pd.read_csv(path)
    return data.tail()


if __name__ == "__main__":
    path = './assets/addresses.csv'
    print(read_using_DictReader(path))
    print(read_by_pandas_head(path))
    print(read_by_pandas_tail(path))
