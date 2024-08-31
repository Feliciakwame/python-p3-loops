#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>0:
        print(i)
        i=i-1
        print("Happy New Year!")
        
    pass

def square_integers(int_list):
    int_list=[1,2,3,4,5,]
    square_integers = [x**2 for x in int_list]
    return square_integers
    

def fizzbuzz():
    i=0
    for i in range(1,101):
    
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
    
    pass
