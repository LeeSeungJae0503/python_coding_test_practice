def solution(age):
    age_list = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}
    answer = ''
    for i in str(age):
        answer += age_list[int(i)]
    return answer