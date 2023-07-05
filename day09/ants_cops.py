def solution(hp):
    power5 = hp // 5
    power3 = (hp - (5*power5)) // 3
    power1 = (hp - (5*power5) - (3*power3)) // 1
    return power5 + power3 + power1
