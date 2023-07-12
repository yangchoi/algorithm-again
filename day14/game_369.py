def solution(order):
    counted_numbers = ['3', '6', '9']
    count = 0
    for i in list(str(order)):
        if i in counted_numbers:
            count += 1
    return count
