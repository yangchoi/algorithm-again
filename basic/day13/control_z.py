def solution(s):
    stack = []
    for num in s.split(' '):
        try:
            stack.append(int(num))
        except:
            # z일 경우 pop해주어 바로 전에 append 한 숫자를 stack에서 제거
            stack.pop()
    return sum(stack)
