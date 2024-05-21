def discount_hash(discount):
    table = dict.fromkeys(discount, 0)
    for d in discount:
        if d in table:
            table[d] += 1

    return table


def zip_hash(want, number):
    return {w: n for w, n in zip(want, number)}


def solution(want, number, discount):
    want_table = zip_hash(want, number)
    n = len(discount)
    days = 10

    for i in range(n - days + 1):
        current_window = discount[i:i + days]
        discount_table = discount_hash(current_window)
        if all(discount_table.get(w, 0) == want_table[w] for w in want_table):
            return i + 1
    return 0


# 10일간 구매 가능한 수량을 고려하지 않아서 fail