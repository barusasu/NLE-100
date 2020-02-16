import numpy as np

path = '../data/hightemp.txt'

with open(path) as f:
    l = []
    for s in f.readlines():
        l.append(s.replace('\t', ' ').strip().split())
    nl = np.array(l)
    unique, counts = np.unique(nl[:, 0], return_counts=True)

    ul_unique = []
    for u, c in zip(unique, counts):
        ul_unique.append([u, c])
    ul_unique_sorted = sorted(ul_unique, key=lambda x: x[1], reverse=True)
    print(ul_unique_sorted)