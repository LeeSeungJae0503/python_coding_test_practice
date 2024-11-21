def solution(array):
    largest = sorted(array, reverse=True)[0]
    solution = [largest, array.index(largest)]
    return solution

"""
def solution(array):
    return [max(array), array.index(max(array))]
"""