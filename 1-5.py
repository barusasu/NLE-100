s = 'I am an NLPer'

def n_gram(target, n):
    return [target[i:i+n] for i in range(len(target)-1)]

print(n_gram(s, 2))
print(n_gram(s, 3))

word = s.split()
print(n_gram(word, 2))
print(n_gram(word, 3))