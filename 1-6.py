def n_gram(target, n):
    return {target[idx:idx+n] for idx in range(len(target)-1)}

x_str = 'paraparaparadise'
y_str = 'paragraph'

X = n_gram(x_str, 2)
Y = n_gram(y_str, 2)
print('X : {}'.format(X))
print('Y : {}'.format(Y))
print('和集合 : {}'.format(X | Y))
print('差集合 : {}'.format(X - Y))
print('積集合 : {}'.format(X & Y))
print("in 'se' :{}".format('se' in X))
print("in 'se' :{}".format('se' in Y))