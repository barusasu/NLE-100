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
(.+?) 非貪欲でマッチさせ、後ろの'='を含まないようにする
'''
r = re.compile(r'(=+)(.+?)(=+)')
doc = article_UK().split('\n')

for line in doc:
    match = r.match(line)
    if match:
        print('セクション：{section}, レベル:{level}'.format(section=match.group(2).strip(' '), level=len(match.group(1))-1))