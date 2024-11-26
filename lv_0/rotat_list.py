def solution(numbers, direction):
    answer = []
    if direction == 'left':
        answer = numbers[1:]
        answer.insert(len(numbers), numbers[0])
    else:
        answer = numbers[:-1]
        answer.insert(0, numbers[-1])
    return answer

"""
def solution(numbers, direction):
    if direction == 'left':
        return numbers[1:] + numbers[:1]
    else:
        return numbers[-1:] + numbers[:-1]
"""