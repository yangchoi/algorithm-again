def solution(age):
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    answer = ''

    for i in str(age):
        answer += words[int(i)]
    return answer
