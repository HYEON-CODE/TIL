import re


def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    answer = ""
    new_id = new_id.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 
    # 제외한 모든 문자를 제거합니다.
    for i in new_id:
        if i.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.':
            answer+=i
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    answer = re.sub('[.]{2,}', '.', answer)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    answer = re.sub('^[.]|[.]$', '', answer)
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer=='':
        answer = 'a'
    # 6단계 new_id의 길이가 16자 이상이면, 
    # new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) >= 16:
        new_id=""
        for i in range(15):
            if i==14 and answer[i]=='.':
                pass
            else: new_id+=answer[i]
        answer=new_id
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 
    # new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.        
    if len(answer)<=2:
        index=len(answer)-1
        while len(answer)<3:
            answer+=answer[index]
    return answer
