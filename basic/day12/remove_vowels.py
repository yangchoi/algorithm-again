def solution(my_string):
    vowels = ['i', 'e', 'a', 'o', 'u']
    for i in list(my_string):
        if i in vowels:
            my_string = my_string.replace(i, '')
    return my_string
