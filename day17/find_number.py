def solution(num, k):
    num_list = list(map(int, str(num)))
    if k in num_list:
        return num_list.index(k) + 1
    else:
        return -1