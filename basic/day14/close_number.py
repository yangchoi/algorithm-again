def solution(array, n):
    new_list = []
    for i in array.sort():
        new_list.append(abs(n - i))
    answer = [array[new_list.index(min(new_list))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]
