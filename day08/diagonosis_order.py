def solution(emergency):
    new_array = sorted(emergency, reverse=True)
    new_order = []

    for i in emergency:
        new_order.append(new_array.index(i) + 1)
    return new_order
