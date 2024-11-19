def solution(hp):
    count = 0
    count += hp // 5
    hp %= 5

    count += hp // 3
    hp %= 3

    count += hp

    return count

"""
def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
"""