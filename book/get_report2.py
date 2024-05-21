from collections import defaultdict

def solution(id_list, report, k):
    # 각 유저별로 신고한 사람 목록 정리
    reports_by_user = defaultdict(set)

    # 각 유저가 신고당한 횟수 정리
    report_counts = defaultdict(int)

    # 신고 내역 처리
    for entry in report:
        reporter, reported = entry.split()
        if reported not in reports_by_user[reporter]:
            reports_by_user[reporter].add(reported)
            report_counts[reported] += 1

    # 정지된 유저 목록 (k 보다 많은 경우에만 기록)
    suspended_users = {user for user, count in report_counts.items() if count >= k}

    # 각 유저별 받은 정지 결과 통지 횟수 정리
    result = [0] * len(id_list)
    id_index = {id: idx for idx, id in enumerate(id_list)}

    for reporter, reported_users in reports_by_user.items():
        for reported in reported_users:
            if reported in suspended_users:
                result[id_index[reporter]] += 1

    return result