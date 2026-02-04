import sys
import os
import pandas as pd
import numpy as np


def fail(msg):
    print("Error:", msg)
    sys.exit(1)


def main():
    args = sys.argv

    if len(args) != 5:
        fail("Usage: topsis <input.csv> <weights> <impacts> <output.csv>")

    inp = args[1]
    wts = args[2]
    imps = args[3]
    out = args[4]

    if not os.path.isfile(inp):
        fail("Input file not found")

    try:
        df = pd.read_csv(inp)
    except:
        fail("Cannot read input file")

    if df.shape[1] < 3:
        fail("Input file must have at least 3 columns")

    mat = df.iloc[:, 1:].values

    if not np.issubdtype(mat.dtype, np.number):
        fail("Columns must be numeric")

    w = wts.split(',')
    imp = imps.split(',')

    n = mat.shape[1]

    if len(w) != n or len(imp) != n:
        fail("Weights, impacts and columns count mismatch")

    try:
        w = np.array(w, dtype=float)
    except:
        fail("Weights must be numbers")

    for i in imp:
        if i not in ['+', '-']:
            fail("Impacts must be + or -")

    den = np.sqrt((mat ** 2).sum(axis=0))
    norm = mat / den

    wmat = norm * w

    best = []
    worst = []

    for i in range(n):
        if imp[i] == '+':
            best.append(wmat[:, i].max())
            worst.append(wmat[:, i].min())
        else:
            best.append(wmat[:, i].min())
            worst.append(wmat[:, i].max())

    best = np.array(best)
    worst = np.array(worst)

    dpos = np.sqrt(((wmat - best) ** 2).sum(axis=1))
    dneg = np.sqrt(((wmat - worst) ** 2).sum(axis=1))

    score = dneg / (dpos + dneg)
    rank = score.argsort()[::-1] + 1

    df["Topsis Score"] = score
    df["Rank"] = rank

    df.to_csv(out, index=False)
    print("TOPSIS completed successfully.")


if __name__ == "__main__":
    main()
