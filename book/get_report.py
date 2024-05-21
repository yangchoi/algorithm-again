from collections import defaultdict


def solution(id_list, report, k):
    # 각 유저별로 신고당한 횟수 정리
    report_counts = {}
    for id in id_list:
        report_counts[id] = 0

    for status in report:
        id = status.split(' ')[1]
        if id in report_counts:
            report_counts[id] += 1

    return list(report_counts.values())


# 예외에 대한 처리 부족