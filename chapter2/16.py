path = '../data/hightemp.txt'

n = int(input('自然数を入力してください : '))

with open(path) as f:
    l = f.readlines()
    gyou = (len(l) + n - 1) // n
    for i in range(n):
        for j in range(i*gyou, i*gyou + gyou):
            if len(l) != j:
                print(l[j].strip('\n'))
        print('------------------------------')
    