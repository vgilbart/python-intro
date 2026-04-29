#!/usr/bin/env python3

import argparse
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

# Deal with arguments
parser = argparse.ArgumentParser()
parser.add_argument('--filename', action="store", required=True)
args = parser.parse_args()
print("Filename is: " + args.filename)

if __name__ == "__main__":
    main(args.filename)