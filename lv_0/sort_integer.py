def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))

    return sorted(answer)

"""
def solution(my_string):
    return sorted[int(i) for i in my_string if i.isdigit()]
"""