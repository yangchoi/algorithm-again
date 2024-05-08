def solution(array):
    answer = []
    sorted_array = sorted(array, reverse=True)
    answer.append(sorted_array[0])
    answer.append(array.index(sorted_array[0]))
    return answer
