def solution(cipher, code):
    answer = ''
    for i in range(code, len(cipher)+1, code):
        answer += cipher[i-1]
    return answer

'''
def solution(cipher, code):
    return cipher[code-1::code]
'''