#프로그래머스 이상한 문자 만들기
#느낀 점: 문제를 풀기 전에 어떤 함수를 쓸 것인지 먼저 생각하고, 내용을 구상한 후 코딩을 한다.
def solution(s):
    s=s.split(' ')
    result=list()
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2==0:
                result.append(s[i][j].upper())
            else:
                result.append(s[i][j].lower())
        if not i==len(s)-1:
            result.append(' ')
    return(''.join(result))

#K번째 수
#느낀 점: 자주쓰는 내장 함수에 대해 다시 찾아볼 필요가 없이 완전히 이해하는 게 중요하다.
def solution(array, commands):
    result = []
    for command in commands:
        array_n = array[command[0]-1:command[1]]
        array_n.sort()
        result.append(array_n[command[2]-1])
    return result

#로또의 최고 순위와 최저 순위
#예외처리를 잘해야 될 거 같다. 맞다고 생각했던 것도 예상치 못한 예외가 등장한다.
def solution(lottos, win_nums):
    result=[]
    rank = 7
    count = 0
    for lotto in lottos:
        if lotto in win_nums:
            rank -= 1
        elif lotto == 0:
            count += 1
    if rank-count==7:
        result.append(6)
    else:
        result.append(rank-count)
    if rank==7:
        rank=6
    result.append(rank)
    return result