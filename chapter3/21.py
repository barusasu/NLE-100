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
re.compile()で正規表現パターン文字列をコンパイルして正規表現パターンオブジェクトを生成。
findall() マッチする部分全てをリストで取得。
----------------------------------------
正規表現
. 改行以外の任意の1文字
* 直前のパターンを0回以上繰り返し
'''
pattern = re.compile(r'\[\[Category:.*\]\]')
result = pattern.findall(article_UK())
for line in result:
    print(line)
