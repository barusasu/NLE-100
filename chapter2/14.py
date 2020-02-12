path = '../data/hightemp.txt'

n = int(input('自然数を入力してください : '))

with open(path) as f:
    l = f.readlines()
    for s in range(0,n):
        print(l[s].strip('\n'))

'''
head -n 5 ../data/hightemp.txt
で確認
'''