def solution(n, numlist):
    multiple_list = []
    for num in numlist:
        if num % n == 0:
            multiple_list.append(num)
    return multiple_list
        