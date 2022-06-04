from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        file_csv = csv.reader(file, delimiter=",")
        head, *tail = file_csv
        result = []

        for line in tail:
            current_line = {}
            for i, column in enumerate(head):
                current_line[column] = line[i]
            result.append(current_line)
    return result
