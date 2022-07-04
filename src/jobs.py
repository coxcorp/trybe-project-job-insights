import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs = list(csv.DictReader(file))
        return jobs
