def solution(num, k):
    num_str = str(num)
    position = num_str.find(str(k))
    return position + 1 if position != -1 else -1