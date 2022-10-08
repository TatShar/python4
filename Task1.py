
# from math import pi

# p=str(pi)
# d= float (input ('d='))
# d1=repr(d)
# l=len(d1)
# print(p[:l])

from decimal import Decimal

def accuracy (num,d):
    number = Decimal(f'{num}')
    return number.quantize(Decimal(f'{d}'))
number=float(input('Input a number '))
d=float(input ('imput bit depth '))
print (accuracy(number,d))

