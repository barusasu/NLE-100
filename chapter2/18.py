import numpy as np

path = '../data/hightemp.txt'

'''
np.argsort()で基準となる行または列のインデックスを取得し、
それに従って行・列を並び替える
'''
with open(path) as f:
    l = []
    for s in f.readlines():
        l.append(s.replace('\t', ' ').strip().split())
    nl = np.array(l)
    nl_sorted = nl[np.argsort(nl[:, 2])]
    print(nl_sorted)  