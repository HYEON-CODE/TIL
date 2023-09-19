#프로그래머스 코딩테스트 준비
# 1단계 : 8문제
# 1. 추억 점수 176963 2. 카드 뭉치 159994 3. 덧칠하기 161989 4. 폰켓몬 1845 5. 2016년 12901 6. 가운데 글자 가져오기 12903 7. 같은 숫자는 싫어 12906 8. 나누어 떨어지는 숫자 배열 12910

#2
def solution(cards1, cards2, goal):
    for i in goal:
        try:
            if cards1[0]==i:
                cards1.pop(0)
                continue
        except:
            pass
        try:
            if cards2[0]==i:
                cards2.pop(0)
                continue
        except:
            return "No"
        return "No"
    return "Yes"
# 문장의 길이를 먼저 확인하면 에러가 발생하지 않는다.
