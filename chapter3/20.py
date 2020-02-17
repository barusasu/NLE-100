import gzip
import json

path = '../data/jawiki-country.json.gz'

'''
gzip圧縮されたファイルをgzip.open()で解凍。
json.loads()でJSON形式を辞書型に変換。
'''
with gzip.open(path, mode='r') as f:
    for line in f:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            print(obj['text'])