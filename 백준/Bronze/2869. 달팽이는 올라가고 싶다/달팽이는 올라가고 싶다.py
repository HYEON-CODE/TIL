a, b, v = map(int, input().split())
c = a - b
if (v - a) == 0:
    print(1)
else:
    v = v - a
    if v%c>0:
        print(v // c + 2)
    else:
        print(v // c + 1)