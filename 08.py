def cipher(target):
    '''
    chr()
    Unicodeコードポイントを文字に変換

    ord()
    文字をUnicodeコードポイントに変換
    '''
    result = ''
    for i in target:
        if 'a' <= i and i <= 'z':
            result += chr(219-ord(i))
        else:
            result += i
    return result

s = 'abCDEfjhIjk'
result1 = cipher(s)
print(result1)
result2 = cipher(result1)
print(result2)