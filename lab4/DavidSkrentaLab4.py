'''
CIS 117 Python Programing: Lab 4
David Skrenta
'''

def savings(cost, coupon_rate):
    return round(cost * coupon_rate, 2)

def coupon(cost):
    if cost < 10:
        return 0.00
    elif 10 <= cost < 60:
        return 0.08
    elif 60 <= cost < 150:
        return 0.10
    elif 150 <= cost < 210:
        return 0.12
    elif cost >= 210:
        return 0.14

cost = input("Please enter the cost of your groceries: ")
coupon_rate = coupon(int(cost))
savings = savings(int(cost), coupon_rate)
print("You win a discount coupon of $" + str(savings) +
". (" + str(round(coupon_rate * 100)) + "% of your purchase)")

'''
Please enter the cost of your groceries: 5
You win a discount coupon of $0.0. (0% of your purchase)

Please enter the cost of your groceries: 15
You win a discount coupon of $1.2. (8% of your purchase)

Please enter the cost of your groceries: 100
You win a discount coupon of $10.0. (10% of your purchase)

Please enter the cost of your groceries: 165
You win a discount coupon of $19.8. (12% of your purchase)

Please enter the cost of your groceries: 365
You win a discount coupon of $51.1. (14% of your purchase)
'''
