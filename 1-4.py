s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
l = [x.strip('. ') for x in s.split()]
print(l)

"""

update()
引数に別の辞書オブジェクトを指定すると、その辞書オブジェクトの要素が全て追加される。

"""
new_l = {}
for index, value in enumerate(l):
    if index + 1 in (1,5,6,7,8,9,15,16):
        new_l.update({(value[:1], index+1)})
    else:
        new_l.update({(value[:2], index+1)})
print(new_l)

print(new_l['Be'])