st = list(input()) # 문자열
del_st = list(input()) # 폭발문자열
stack = []
for i in st:
    stack.append(i)
    if stack[len(stack)-len(del_st):len(stack)]==del_st:
        for _ in range(len(del_st)):
            stack.pop()
print(''.join(stack) if len(stack)!=0 else 'FRULA')