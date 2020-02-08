import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = [x for x in s.split()]
result = []
for word in words:
    if len(word) > 4:
        shuffle_list = list(word[1:-1])
        # shuffle()　引数のリストをシャッフルする
        random.shuffle(shuffle_list)
        # リストを文字列と連結するにはjoin()を使う
        # ''.join()で単純連結
        result.append(word[0] + ''.join(shuffle_list) + word[-1])
    else:
        result.append(word)

print(result)