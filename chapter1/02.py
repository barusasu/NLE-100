s_1 = 'パトカー'
s_2 = 'タクシー'

# 文字列の長さが異なるとエラー
# new_s = "".join(s_1[idx]+s_2[idx] for idx in range(len(s_1)))

# zip関数
# 文字列の長さが異なる場合、短い方に合わせる
new_s = ''
for f, s in zip(s_1, s_2):
    new_s += f + s
print(new_s)