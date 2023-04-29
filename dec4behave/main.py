from os import getcwd
import csv
from collections import Counter

csv_path = getcwd() + "/Resources/BeerCans.csv"
feature_path = getcwd() + "/Tests/BeerCans.feature"


def insert_to_feature_file(func):
    def inner1(*args, **kwargs):
        row = "\n"
        with open(feature_path) as f:
            content = f.readlines()
            for i, item in enumerate(content):
                if "Examples:" in item:
                    row = content[i + 1]
                    for k, v in kwargs.items():
                        k = k.replace("_", " ")
                        if len(k) > len(v):
                            temp = len(k) - len(v)
                            spaces = " " * temp
                            row = row.replace(k, v + spaces)
            f.close()
        with open(feature_path, "a") as f:
            f.write(row)
            f.close()
        func(*args, **kwargs)

    return inner1


@insert_to_feature_file
def read_args(*args, **kwargs):
    pass


with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i, row in enumerate(csv_reader):
        if i == 0:
            pass
        else:
            read_args(opening_balance=row[0], processed=row[1], in_stock=row[2])
