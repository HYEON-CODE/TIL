n = int(input())
result = 0
for i in range(n):
    words = input()
    last_word = ""
    exist_word = list()
    for word in words:
        if (last_word==word):
            continue
        elif (last_word!=word and word not in exist_word):
            exist_word.append(word)
            last_word=word
        else:
            result -= 1
            break
    result +=1
print(result)