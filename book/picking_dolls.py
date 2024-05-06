def solution(board, moves):
    # 각 열의 인형을 거꾸로 저장하는 리스트
    # len(board[0]) : 열의 개수, 각 열마다 하나의 리스트 할당받기
    lanes = [[] for _ in range(len(board[0]))]

    # board 를 역순으로 탐색, 각 열의 인형을 lanes 에 추가
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])

    # 인형을 담을 bucket
    bucket = []

    # 사라진 인형의 총 개수 저장할 변수
    answer = 0

    for m in moves:
        if lanes[m - 1]:  # 해당 열에 인형이 있는 경우
            doll = lanes[m - 1].pop()

            if bucket and bucket[-1] == doll:  # 바구니에 인형이 있고 가장 위에 있는 인형과 같은 경우
                bucket.pop()
                answer += 2
            else:  # 바구니에 인형이 없거나, 가자아 위에 있는 인형과 다른 경우
                bucket.append(doll)

    return answer