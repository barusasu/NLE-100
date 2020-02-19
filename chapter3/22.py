import gzip
import json
import re

path = '../data/jawiki-country.json.gz'

def article_UK():
    with gzip.open(path, mode='r') as f:
        for line in f:
            obj = json.loads(line)
            if obj['title'] == 'イギリス':
                return obj['text']
    raise ValueError('イギリスの記事が見つからない')

'''
正規表現で()は中身を取り出すことができる。
re.match()では()で抽出した箇所の文字列を得ることができる。
match.group(1)はマッチした1番目のグループ。
match.group(1)は'category_name'または
'category_name|sort_key'になっているから
　|　で文字列を分割して先頭の文字列を取り出す
'''
r = re.compile('\[\[Category:(.+)\]\]')
doc = article_UK().split('\n')
for line in doc:
    match = r.match(line)
    if match:
        print(match.group(1).split('|')[0])