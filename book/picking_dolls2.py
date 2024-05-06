def solution(board, moves):
    # 각 인형들을 넣을 lanes 들이 필요하다.
    lanes = [[] for _ in range(len(board[0]))]

    # 가로
    for i in range(len(board) -1, -1, -1):
        # 세로
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])

    dolls = [] # 인형을 넣을 곳
    answer = 0
    for m in moves:
        if lanes[m - 1]:
            doll = lanes[m - 1].pop()

            if dolls and dolls[-1] == doll:
                dolls.pop()
                answer += 2
            else:
                dolls.append(doll)

    return answer

