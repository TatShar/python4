import random

def new_list (number):
   
    lst=[]
    for i in range(a):
        lst.append(random.randint(1,5))
    print (lst)
    lst_new=[]
    count=0
    for i in lst:
        if lst.count(i)==1:
            lst_new.append(i)
    return lst_new
a=int(input('Input a number '))
print(new_list(a))


