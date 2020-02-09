path = 'data/hightemp.txt'
'''
withブロックを使うとブロック終了時に自動でclose()される。

readlines()
開いたファイル全体を行ごとに分割したリストとして取得できる。
改行コード\nを含んだ文字列が要素となる。

'''
with open(path) as f:
    l = f.readlines()
    print(len(l))

# wc -l data/highttemp.txt　で確認
# 24 data/hightemp.txt