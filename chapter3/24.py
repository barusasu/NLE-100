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

r = re.compile(r'ファイル:(.+?)\|')
doc = article_UK().split('\n')
for line in doc:
    match = r.match(line)
    if match:
        print(match.group(1))