def solution(array):
    array.sort()
    middle = len(array) / 2 - 1 if len(array) % 2 == 0 else len(array) / 2
    return array[int(middle)]

"""
def solution(array):
    return sorted(array)[len(array) // 2]
"""