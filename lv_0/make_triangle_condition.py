def solution(sides):
    max_length = max(sides)
    sides.remove(max_length)
    if max_length >= sum(sides):
        return 2
    else:
        return 1
    
"""
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sieds)) else 2
"""