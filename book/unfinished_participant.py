def solution(participant, completion):
    # key: 이름, value: 이름 갯수
    table = {}

    for c in completion:
        if c in table:
            table[c] += 1
        else:
            table[c] = 1

    for p in participant:
        if p not in table or table[p] == 0:
            return p
        table[p] -= 1