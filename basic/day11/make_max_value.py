def solution(numbers):
    sorted_nums = sorted(numbers)
    return sorted_nums[len(sorted_nums) - 1] * sorted_nums[len(sorted_nums) - 2]
