#1.write a program to find reverse of a string using while loop?

# a=input('enter word')
# i=len(a)-1
# while i>=0:
#     print(a[i],end='')
#     i-=1

#2.check whether the string is pallindrome or not?

# a=input('enter word')
# b=len(a)-1
# tem=a
# i=len(tem)-1
# while (i>0):
#     i=i-1
# if tem[i]==a[b]:
#     print('palandrome')
# else:
#     print('not palandrome')

#3.find the area of triangle?

# h=int(input('enter height of triangle'))
# b=int(input('enter base of triangle'))
# print('area=',1/2*b*h)

#4.find the iteration variable in the following python code?

#ans: letter

#6.write the following python code printout?
#ans:49

#7.how would you print out the following variable into upper case in python?
#Greet=Hello World

# a='Greet=Hello world'.upper()
# print(a)

#8.what is the out of following python code?
# a='hello'
# b='welocome'
# print(a+b)

# ans:hellowelcome

#9.find the program print out?
# x='40'
# y=int(x)+2
# print(y)

#ans:42

#10.print the given series using for loop?

# for i in range(100,9,-10):
#     print(i,end=' ')

#11.write a program to calculate the electricity(accept number of unit from user)according to the following criteria?

# a=int(input('enter the unit'))
# if a<=100:
#     print('total bill amount is 0')
# elif 100<a<=200:
#     x=a-100
#     print('total bill amount is',x*5)
# elif a>200:
#     y=a-200
#     print('total bill amount is',(y*10)+500)

#12.write a program to check whether the last digit of a number(enter a user) is divisible by 3 or not

# a=int(input('enter a number'))
# b=a%10
# if b%3==0:
#     print('last digit of',a,'is divisible by 3')
# else:
#     print('last digit of',a,'is not divisible by 3')

#13.write the output of the following if a=9?

#ans:hello

#14.accept the age(m,f),number of days and display the wages accordingly?

#a=int(input('enter age'))
#b=(input('select your sex f/m'))
# c=int(input('enter working days'))
#if 18<=a<30:
#   if b=='m':
#     print('your wage is',c*700)
#    elif b=='f':
#        print('your wage is',c*750)
#elif 30<=a<=40:
#    if b == 'm':
#        print('your wage is', c*800)
#   elif b == 'f':
#        print('your wage is', c*850)
#else:
#    print('invalid input')

#15.write a rogram to find factorial of a number using while loop

# num=int(input("enter the number"))
# i=1
# while (num>0):
#     i=i*num
#     num-=1
# print("factorial=",i)

#write a program to print the given output?
#input=hello

# a='hello'
# b=int(len(a))
# for i in range(b+1):
#     for j in range(i):
#         print(a[j],end='')
#     print()