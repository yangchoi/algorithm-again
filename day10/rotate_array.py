from collections import deque
# deque: 양방향 큐
# 앞 뒤로 엘리먼트 추가 및 제거 가능


def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)  # rotate: deque의 요소를 num만큼 회전시킴
    else:
        numbers.rotate(-1)
    return list(numbers)
