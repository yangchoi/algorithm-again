def solution(my_string, letter):
    str_list = list(my_string)
    for str in my_string:
        if str == letter:
            str_list.remove(letter)
    return ''.join(str_list)
