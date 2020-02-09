path_r = '../data/hightemp.txt'
path_w = '../output/result.txt'

'''
readlines()で行ごとに分割したリストを取得し、
replace()で各行のタブ(\t)をスペースに置換。
置換結果をresult.txtに書き込み
'''
with open(path_r) as f:
    result = []
    for l in f.readlines():
        result.append(l.replace('\t', ' '))

with open(path_w, mode='w') as f:
    f.writelines(result)

# Unixコマンド sedで確認 正規表現で置換処理
# sed 's/\t/ /g' ../data/hightemp.txt
# s: 置換
# g: gがない場合、1行のうち初めにマッチしたもののみが置換される