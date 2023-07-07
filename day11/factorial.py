import math


def solution(n):
    answer = []
    for i in range(1, n+1):
        if math.factorial(i) > n:
            return answer[len(answer) - 1]
        if math.factorial(i) <= n:
            answer.append(i)
    return answer[len(answer) - 1]
