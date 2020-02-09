s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

"""

split()
文字列を指定の区切り文字で分割し、リストとして取得できる
指定しない場合、空白文字で区切る。

strip()
文字列の先頭・末尾の余分な文字を削除するメソッド
引数を省略すると空白文字が削除された文字列を返す。
引数を与えると与えた文字が削除された文字列を返す。空白も削除する場合、スペースも追加する必要がある。

"""
new_str = [x.strip(',. ') for x in s.split()]
# print(new_str)

l_new_str = [len(l) for l in new_str]
print(l_new_str)
