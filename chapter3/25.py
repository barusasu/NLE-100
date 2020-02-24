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
    raise ValueError('Error')

r = re.compile(r'\|(.+?) = (.+)')

doc = article_UK().split('\n')
basic_info = {}
for line in doc:
    match = r.match(line)
    if match:
        basic_info[match.group(1)] = match.group(2)
        
# 確認用
for key, val in basic_info.items():
    print('{} : {}'.format(key, val))