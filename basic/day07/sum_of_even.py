def solution(n):
    even_list = []
    for i in range(n+1):
        if i % 2 == 0:
            even_list.append(i)
    return sum(even_list)
