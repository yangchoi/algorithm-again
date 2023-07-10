def solution(my_string):
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = []
    for i in list(my_string):
        if i in number_list:
            answer.append(int(i))
    return sorted(answer)
