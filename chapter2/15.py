path = '../data/hightemp.txt'

n = int(input('自然数を入力してください : '))

with open(path) as f:
    l = f.readlines()
    for i in range(len(l)-n, len(l)):
        print(l[i].strip('\n'))

'''
tail -n 5 ../data/hightemp.txt
で確認
'''