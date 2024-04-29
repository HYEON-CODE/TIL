fib_count = 1
def fib(n):
    global fib_count
    if (n==1 or n==2):
        return 1
    else:
        fib_count+=1
        return fib(n-1) + fib(n-2)
    
fibonacci_count = 0
def fibonacci(n):
    global fibonacci_count
    dp = [0]*50
    dp[1]=1
    dp[2]=1
    for i in range(3, n+1):
        fibonacci_count+=1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
fib(n)
fibonacci(n)
print(fib_count, fibonacci_count)