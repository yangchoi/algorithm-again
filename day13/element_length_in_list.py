def solution(strlist):
    str_length = []
    for str in strlist:
        str_length.append(len(list(str)))
    return str_length
