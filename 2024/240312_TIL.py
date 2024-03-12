def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer+=int(i)
    return answer

# Level.1 문제 1
def solution(nums):
    answer = len(list(set(nums)))
    if answer > (len(nums)//2):
        answer=len(nums)//2
    return answer

# Level.1 문제 2
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    for i in range(1, len(score)//m+1):
        answer += score[i*m-1] * m 
    return answer

# Level.2 문제 1 망버전
# 정렬부분에서 실패해서 모든 정렬 공부하고 다시 시험보겠다.
# 문제 1 1번째 시도
def solution(s):
    s = list(s)
    while len(s)!=0: # len이 0이면 반복문 종료
        for i in range(len(s)-1):
            if s[i]==s[i+1]: #앞뒤가 같다면 삭제
                del s[i:i+2]
                i -= 2
                continue
            elif i == len(s)-2:
                return 0
    return 1
# 문제 1 2번째 시도 index사용해서 마지막 삭제까지 가려했는데 막혔다.
def solution(s):
    s = list(s)
    end = len(s)-1
    while end > 0: # 0이면 끝
        last_del = 0
        for i in range(end):
            if s[i] == s[i + 1]:
                del s[i:i+2]
                last_del = i
        end = last_del
        print(s)

# 그리디 알고리즘 거스름돈 문제
