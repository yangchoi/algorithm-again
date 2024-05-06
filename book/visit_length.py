def check_border(spot):
    x, y = spot
    x = max(min(x, 5), -5)
    y = max(min(y, 5), -5)
    # min(x, 5) > x값과 5를 비교해 둘 중 더 작은 값 반환
    # x가 5보다 클 경우 5를 반환하고 아닌 경우 x를 반환
    # max(결과, -5) > 결과값과 -5를 비교해 둘 중 더 큰 값을 반환
    # 결과값이 -5보다 작을 경우 -5를 반환하고 아닌 경우 결과값을 반환
    return (x, y)


def solution(dirs):
    visited_paths = set()
    spot = (0, 0)
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    for d in dirs:
        next_spot = check_border((spot[0] + moves[d][0], spot[1] + moves[d][1]))

        if spot != next_spot:
            path = tuple(sorted([spot, next_spot]))
            # spot, next_spot을 기반으로 순서 상관없이 일관된 방식으로 경로 표현하기
            # 경로를 정렬하고 튜플로 저장해 두 지점 사이를 오가는 이동이 동일한 경로로 인식되도록함
            # spot에서 next_spot으로 가는 이동이 next_spot에서 spot으로의 이동과 동일하게 처리되도록 하기 위함
            # (2, 2)에서 (1, 1)로 이동한 것과 (1, 1)에서 (2, 2)로 이동한 것을 모두 같은 경로로 이동한 것으로 간주하여 중복 방지
            visited_paths.add(path)
            spot = next_spot

    return len(visited_paths)
