# BOJ 1541번 잃어버린 괄호
n = input().split('-')
for i in range(len(n)):
    for j in n[i]:
        temp = list()
        if j in '+':
            temp = n[i].split('+')
            res = [i.lstrip('0') for i in temp]
            res = '+'.join(res)
            n[i] = str(eval(res))
            break
res = [i.lstrip('0') for i in n]
print(eval('-'.join(res)))