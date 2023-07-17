def solution(my_string):
    splited_string = my_string.split()
    answer = int(splited_string[0])
    for i in range(1, len(splited_string), 2):
        if splited_string[i] == '+':
            answer += int(splited_string[i + 1])
        else:
            answer -= int(splited_string[i + 1])
    return answer
