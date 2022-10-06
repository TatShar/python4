import decimal
from decimal import getcontext, Decimal

# Вычислить число c заданной точностью d

number_str = str(input ('number = '))
d_str = str(input('Input d= '))
len_num = len(number_str)
len_d=len(d_str)
i=-1
if len_num>len_d:
    razn=len_num-len_d
    print(float(number_str[:-razn]))
elif len_num<len_d:
    razn=len_d-len_num
    while razn>0:
        number_str=number_str+'0'
        razn-=1
    number_dec=Decimal(number_str)
    print(number_dec)
else: 
    number_dec=Decimal(number_str)
    print (number_dec)
    
