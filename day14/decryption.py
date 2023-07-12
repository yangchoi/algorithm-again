def solution(cipher, code):
    cipher_list = list(cipher)
    answer = []
    for i in range(code-1, len(cipher_list), code):
        answer.append(cipher_list[i])
    return ''.join(answer)
