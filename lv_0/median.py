# sort는 반환값이 없고 sorted는 반환값이 존재한다. 
# sorted는 새로운 정렬된 리스트를 반환한다. 

def solution(array):
    array.sort()
    middle = len(array) / 2 - 1 if len(array) % 2 == 0 else len(array) / 2
    return array[int(middle)]

"""
def solution(array):
    return sorted(array)[len(array) // 2]
"""