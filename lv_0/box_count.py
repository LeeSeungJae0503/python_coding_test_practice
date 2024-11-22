def solution(box, n):
    sum = 1
    for i in box:
        sum *= i // n
    return sum