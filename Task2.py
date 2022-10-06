# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def simple_multy(number):
    lst=[]
    i=2
    while number>1:
        while number%i==0:
            lst.append(i)
            number=number/i
        i+=1
    lst.insert(0,1)   
    return lst

num=int(input('Input a number '))
print(*simple_multy(num))







