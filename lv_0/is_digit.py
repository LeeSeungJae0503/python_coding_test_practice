def solution(my_string):
    number = [int(num) for num in my_string if num.isdigit()]
    return sum(number)

"""
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
"""