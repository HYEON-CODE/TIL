n = int(input())
x = list(map(int, input().split()))
cp_x = set(x)
cp_x = sorted(list(cp_x))
dict_x = dict()
for index, value in enumerate(cp_x):
    dict_x[value] = index
for i in x:
    print(dict_x[i], end=' ')