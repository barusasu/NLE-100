def func(x, y, z):
    return "{hour}時の{target}は{value}".format(hour=x,target=y,value=z)

s = func(12, '気温', 22.4)
print(s)
