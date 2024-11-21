def solution(n, numlist):
    solution = []
    for i in numlist:
        if i % n == 0:
            solution.append(i)
    return solution

"""
def solution(n, numlist):
    return [num for num in numlist if num % n == 0]
"""