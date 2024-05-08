def solution(n, t):
    current_population = n
    for n in range(t):
        current_population *= 2
    return current_population