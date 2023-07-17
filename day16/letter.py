def solution(message):
    message_list = [i for i in list(message) if i != '']
    return len(message_list) * 2
