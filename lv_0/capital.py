def solution(my_string):
    after = ""
    for i in my_string:
        if i.isupper():
            after += i.lower()
        else:
            after += i.upper()
    return after

print(solution("cccCCC"))