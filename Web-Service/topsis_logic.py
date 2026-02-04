import pandas as pd
import numpy as np

def run_topsis(input_path, weights, impacts, output_path):
    df = pd.read_csv(input_path)

    mat = df.iloc[:, 1:].values.astype(float)
    w = np.array(weights, dtype=float)
    imp = impacts

    den = np.sqrt((mat ** 2).sum(axis=0))
    norm = mat / den
    wmat = norm * w

    best, worst = [], []

    for i in range(len(imp)):
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

    df.to_csv(output_path, index=False)
