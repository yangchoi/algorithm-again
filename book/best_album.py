from collections import defaultdict


def solution(genres, plays):
    # defaultdict : 키가 존재하지 않을 때 자동으로 기본값 생성해줌
    # 키가 존재하지 않을 경우를 체크하고 초기화하는 코드를 작성할 필요가 없어 {} 를 쓰는 것보다 선호
    # {} 를 했을 경우 아래와 같이 초기화 코드가 필요함
    # for i, (genre, play) in enumerate(zip(genres, plays)):
    #     if genre not in genre_play_counts:
    #         genre_play_counts[genre] = 0


    genre_play_counts = defaultdict(int)
    genre_songs = defaultdict(list)

    # 장르별 재생 수와 곡 정보 저장
    for i, (genre, play) in enumerate(zip(genres, plays)):
        # 각 장르별로 play를 더한다.
        genre_play_counts[genre] += play
        # 각 장르에 대해 플레이와, 인덱스를 따로 저장한다.
        genre_songs[genre].append((play, i))

    # 각 장르에 대한 play합을 내림차순으로 정렬 (reverse=True)
    sorted_genres = sorted(genre_play_counts.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for genre, _ in sorted_genres:
        # 해당 장르의 곡을 재생 수 기준으로 내림차순 정렬 (재생 수 같을 경우 인덱스 오름차순)
        # x[0]: 튜플의 첫번째 요소인 play
        # x[1]: 튜플의 두번째 요소인 index
        sorted_genres = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        # -x[0] : play 기준으로 내림차순 정렬, - 기호로 음수로 만들어 큰 값이 앞에 오도록
        # x[1] : 재생 수가 같을 경우, 인덱스를 기준으로 오름차순 정렬
        # 재생 수가 큰 순서대로 정렬
        # 재생 수가 같으면 인덱스가 작은 순서대로 정렬

        # 상위 2개 곡 인덱스를 결과 리스트에 추가
        # extend : 리스트의 끝에 다른 리스트의 모든 요소를 개별적으로 추가
        answer.extend([idx for _, idx in sorted_genres[:2]])

    return answer