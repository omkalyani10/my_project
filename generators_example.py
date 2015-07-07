__author__ = '28164'


def is_prime(number):
    if number == 1:
        return True
    elif number % 2 == 0:
        return False
    else:
        if not [n for n in range(3, number) if number % (n-1) == 0 ]:
            return True

def generator_fetch_prime(number_limit):
    for number in range(number_limit):
        if is_prime(number):
            yield number

def calculate():
    total = 0
    for number in range(103):
        if is_prime(number):
            total += number
            return total

