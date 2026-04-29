#!/usr/bin/env python3

import pandas as pd

def main(filename, min = True, mean = True, max = True):
    data = pd.read_csv(filename, index_col=0)
    stats = {}

    if min:
        stats['min'] = data.min(axis=0).min()
    if mean:
        stats['mean'] = data.mean(axis=0).mean()
    if max:
        stats['max'] = data.max(axis=0).max()

    for key, value in stats.items():
        print(f"{key}: {value}")


filename = input("Enter filename: ")
print("Filename is: " + filename)

if __name__ == "__main__":
    main(filename)