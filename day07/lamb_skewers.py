def solution(n, k):
    if n > 9:
        k = k - n // 10
    return (n * 12000) + (k * 2000)
