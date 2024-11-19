def solution(n):
    if n > 7 and not(n % 7 == 0):
        return n // 7 + 1
    elif n % 7 == 0:
        return n / 7
    else:
        return n % 7
    
"""
def solution(n):
    return (n + 6) // 7
아래 식을 이용해서 올림 효과를 얻을 수 있다. 
(n + (k - 1)) // k
"""