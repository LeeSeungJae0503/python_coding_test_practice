def solution(num_list):
    answer = []
    odd_count, even_count = 0, 0
    for i in num_list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    answer.append(even_count)
    answer.append(odd_count)
    
    return answer

"""
def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n%2] += 1
    return answer
"""