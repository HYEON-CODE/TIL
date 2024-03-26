a, b, c = map(int, input().split())
print(pow(a, b, c))

def pow(a, b, c):
    if (b==0):
        return 1
    elif (b%2 == 0): # b가 짝수라면
        n = pow(a, b//2, c)
        return n * n % c
    else: # b가 홀수라면
        n = pow(a, (b-1)//2, c)
        return a * n * n % c