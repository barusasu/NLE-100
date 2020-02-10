path_r = '../data/hightemp.txt'
path_w1 = '../output/col1.txt'
path_w2 = '../output/col2.txt'

col1 = []
col2 = []
'''
readlines()で行ごとに分割したリストを取得。
split()で各行の要素を分割したリストを取得。
col1に1列目、col2に2列めの要素を追加。
'''
with open(path_r) as f:
    for v in f.readlines():
        l = v.split()
        col1.append(l[0])
        col2.append(l[1])

'''
writelines()でリストを書き込む。
パスを指定しただけだと改行コードが挿入されないので要素がそのまま連結される。
改行コードとjoin()で改行込みの文字列を作成して書き込む
'''
with open(path_w1, mode='w') as f:
    f.write('\n'.join(col1))
with open(path_w2, mode='w') as f:
    f.write('\n'.join(col2))

'''
cutコマンドで確認
cut -f 1 < ../data/hightemp.txt
cut -f 2 < ../data/hightemp.txt
'''