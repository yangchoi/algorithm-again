def solution(record):
    user_table = {}
    for r in record:
        s = r.split(' ')
        status = s[0]
        uid = s[1]
        if status != 'Leave':
            nickname = s[2]
            user_table[uid] = nickname

    answer = []
    for r in record:
        s = r.split(' ')
        status = s[0]
        uid = s[1]
        if status == 'Enter':
            answer.append(f'{user_table[uid]}님이 들어왔습니다.')
        elif status == 'Leave':
            answer.append(f'{user_table[uid]}님이 나갔습니다.')

    return answer

