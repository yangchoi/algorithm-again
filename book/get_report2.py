from collections import defaultdict


def solution(id_list, report, k):
    # 각 유저별로 신고한 사람 목록 정리
    reports_by_user = defaultdict(set)
    """
    reports_by_user =
        {
            "muzi": {"frodo", "neo"},
            "apeach": {"frodo", "muzi"},
            "frodo": {"neo"}
        }
    """

    # 각 유저가 신고당한 횟수 정리
    report_counts = defaultdict(int)
    """
    report_counts = 
        {
            "frodo": 2,
            "neo": 2,
            "muzi": 1
        }
    """

    # 신고 내역 처리
    # 신고한 사람 신고할 사람
    for entry in report:
        reporter, reported = entry.split()
        # 신고자가 신고한 사람 목록에 없다면
        if reported not in reports_by_user[reporter]:
            # 추가
            reports_by_user[reporter].add(reported)
            # 신고 처리
            report_counts[reported] += 1

    # 정지된 유저 목록 (k 보다 많은 경우에만 기록)
    suspended_users = {user for user, count in report_counts.items() if count >= k}

    # 각 유저별 받은 정지 결과 통지 횟수 정리
    result = [0] * len(id_list)
    id_index = {id: idx for idx, id in enumerate(id_list)}

    for reporter, reported_users in reports_by_user.items():
        # reporter : 신고자
        # reported_users : 신고당한 사람 목록
        # reports_by_users.items() 는  reports_by_user 딕셔너리 (키, 값) 쌍 반환
        for reported in reported_users:
            # reported_users는 reporter가 신고한 사용자들 집합
            # 이 집합을 순회하며 각 신고된 사용자가 정지된 사용자인지 확인
            if reported in suspended_users:
                # 정지된 사용자 목록에 reported 사용자가 있다면
                result[id_index[reporter]] += 1
                # 통지 횟수 증가

    return result