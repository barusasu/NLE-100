path_r1 = '../output/col1.txt'
path_r2 = '../output/col2.txt'
path_w = '../output/result.txt'

'''
zip()
複数のリストの要素を取得する。

県名には改行コードが入っているので、
strip()で改行コードを削除。
'''
with open(path_r1) as col1_file, \
        open(path_r2) as col2_file, \
        open(path_w, mode='w') as result:
    for ken, city in zip(col1_file, col2_file):
        result.write(ken.strip('\n') +'\t' + city)

'''
paste ../output/col1.txt ../output/col2.txt
で確認
'''