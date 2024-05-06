def solution(s):
    new_s = []
    for char_s in s:
        # '(' 가 들어올 때만 스택에 추가
        # ')' 가 들어왔을 때 스택에서 여는 괄호 제거
        if char_s == '(':
            new_s.append(char_s)
        else:  # '닫는 괄호'
            if new_s:  # 스택이 비어있지 않으면
                new_s.pop()  # # new_s 스택 마지막 요소 제거
            else:  # 스택이 비어있다면 짝이 맞지않음
                return False

    return len(new_s) == 0


