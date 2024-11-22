def solution(numbers):
    max = sorted(numbers, reverse=True)
    return max[0] * max[1]