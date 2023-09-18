def solution(my_string):
    sorted_str =  sorted(list(my_string.lower()))
    return ''.join(sorted_str)