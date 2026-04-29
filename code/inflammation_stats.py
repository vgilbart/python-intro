#!/usr/bin/env python3

import argparse
import pandas as pd

def main(filename, min = True, mean = True, max = True):
    for file in filename:
        print("Processing file:", file)
        data = pd.read_csv(file, index_col=0)
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
parser.add_argument('--filename', nargs='+', action="store", required=True)
parser.add_argument('--min', action="store_true")
parser.add_argument('--max', action="store_true")
parser.add_argument('--mean', action="store_true")
args = parser.parse_args()

if __name__ == "__main__":
    main(args.filename, min=args.min, mean=args.mean, max=args.max)