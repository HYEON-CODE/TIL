# Level.2 1번 문제
# 이 문제는 좌표의 방문한 점을 세는 게 아니고, 길을 세는 거였다.. ㅜ
def solution(dirs):
    answer = 0
    size = [5, -5]
    ans_x = 0
    ans_y = 0
    visited = [[0 for j in range(size[0]*2)] for i in range(size[0]*2)]
    count = 0
    for i in dirs:
        if i == 'U':
            if ans_y < size[0]:
                ans_y += 1
        elif i == 'D':
            if ans_y > size[1]:
                ans_y -= 1
        elif i == 'R':
            if ans_x < size[0]:
                ans_x += 1
        elif i == 'L':
            if ans_x > size[1]:
                ans_x -= 1
        visited[ans_x][ans_y] = 1
        count += 1
        print(ans_x, ans_y, count)
    
    for i in range(10):
        answer += sum(visited[i])
          
    return answer