def solution(n):
    pizza = 6

    while pizza % n != 0:
        # 사람 인원으로 나누었을 때 나머지가 0이면 피자를 남기지 않고 모두 같은 수의 피자를 먹을 수 있다.
        pizza += 6
    return pizza / 6  # 같은 수가 나누어 떨어질 때까지 피자의 조각수만큼 더해준다.
