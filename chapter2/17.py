import numpy as np
path = '../data/hightemp.txt'

'''
ndarrayに変換し、unique()でユニークな値を抽出。
[:,0]で1列目(県名)を選択して抽出。

'''
with open(path) as f:
    l = []
    for s in f.readlines():
        l.append(s.replace('\t', ' ').strip().split())
    nl = np.array(l)
    print(np.unique(nl[:,0]))

'''
cut --fields=1 ../data/hightemp.txt | sort | uniq > ../output/result.txt
で確認
'''