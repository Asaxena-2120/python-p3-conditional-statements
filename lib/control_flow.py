#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower()=="admin" and password.lower()=="12345":
        return "Access granted" 
    return "Access denied"
    #pass

def hows_the_weather(temperature):
    # your code here
    temp={
        33:"It's brisk out there!",
        55:"It's a little chilly out there!",
        75:"It's perfect out there!",
        99:"It's too dang hot out there!"
    }
    return temp.get(temperature)

def fizzbuzz(num):
    # your code here
    if num%3==0 and num%5==0 :
        return "FizzBuzz"
    elif num%3==0 and num%5!=0:
        return "Fizz"
    elif num%5==0 and num%3!=0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    answers={
        "+":num1+num2,
        "-":num1-num2,
        "*":num1*num2,
        "/":num1/num2,
    }

    if (operation=="+" or operation=="-" or operation=="*" or operation=="/"):
        return answers.get(operation)
    else:
        print("Invalid operation!") 
        return None
    pass
