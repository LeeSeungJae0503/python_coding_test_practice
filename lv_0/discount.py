def solution(price):
    if price >= 100000 and price < 300000:
        return int(price - (price * 0.05))
    elif price >= 300000 and price < 500000:
        return int(price - (price * 0.1))
    elif price >= 500000:
        return  int(price - (price * 0.2))
    else:
        return price
    
"""
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.item():
        if price >= discount_price:
            return int(price * discount_rate)
"""