def solution(order):
    count = 0
    string_order = str(order)
    count += string_order.count('3')
    count += string_order.count('6')
    count += string_order.count('9')
    return count

"""
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
"""