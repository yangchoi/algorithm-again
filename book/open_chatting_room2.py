def solution(record):
    user_table = {}
    actions = []

    for r in record:
        s = r.split(' ')
        action = s[0]
        uid = s[1]

        if action != 'Leave':
            nickname = s[2]
            user_table[uid] = nickname

        if action != 'Change':
            actions.append((action, uid))

    answer = [f'{user_table[uid]}님이 들어왔습니다.'
              if action == 'Enter' else f'{user_table[uid]}님이 나갔습니다.'
              for action, uid in actions]
    return answer
