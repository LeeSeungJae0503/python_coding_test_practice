def solution(n):
    num = str(n)
    sum = 0
    for i in num:
        sum += int(i)
    return sum

"""
def solution(n):
    return sum(int(i) for i in str(n))
"""