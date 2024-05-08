def solution(my_string, n):
    str_list = list(my_string)
    answer = ''
    for str in str_list:
        answer += str * n
    return ''.join(answer)
