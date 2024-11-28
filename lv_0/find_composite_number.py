def solution(n):
    def count_divisors(x):
        count = 0
        for i in range(1, int(x**0.5)+1):
            if (x % i == 0):
                count += 1
                if i != x // i:
                    count += 1
        return count
    composite_count = 0
    for i in range(1, n+1):
        if (count_divisors(i) >= 3):
            composite_count += 1
    return composite_count


"""
def solution(n):
    count = 0
    for i in range(4, n+1):
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                count += 1
                break
    return count
"""