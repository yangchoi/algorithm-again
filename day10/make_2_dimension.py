def solution(num_list, n):
    answer = []
    for num in range(0, len(num_list), n):
        inner_list = []
        for j in range(0, n):
            inner_list.append(num_list[num + j])
        answer.append(inner_list)
    return answer
