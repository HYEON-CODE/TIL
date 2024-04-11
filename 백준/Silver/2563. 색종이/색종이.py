n = int(input())
graph = [[0]*100 for _ in range(100)]
array = [[0, 0] for _ in range(n)]
total_sum = 0

for i in range(n):
    array[i]=list(map(int, input().split()))
for i in array:
    for j in range(10):
        if j+i[1] > 99:
            break
        for k in range(10):
            if k+i[0] > 99:
                break
            graph[j+i[1]][k+i[0]]=1

for row in graph:
    total_sum += sum(row)
print(total_sum)