import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        lista = []
        jobs = csv.DictReader(file)
        for job in jobs:
            lista.append(job)
        return lista
