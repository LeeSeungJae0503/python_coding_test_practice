import math

def solution(n):
    answer = math.sqrt(n)
    if int(answer) ** 2 == n:
        return 1
    else:
        return 2
    
"""
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
"""