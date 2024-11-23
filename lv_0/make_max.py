def solution(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    case = sorted_numbers[0] * sorted_numbers[1]
    case2 = sorted_numbers[-1] * sorted_numbers[-2]
    return case if case > case2 else case2

"""
def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
"""