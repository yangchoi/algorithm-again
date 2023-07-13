def solution(n):
    answer = []
    i = 0
    while i <= n:
        if i % n == 0:
            answer.append(i)
        i += 1
    return answer
