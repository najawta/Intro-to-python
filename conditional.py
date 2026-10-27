# if else
import os

name = input("What is your name?")

age = input("Enter the age:")

if not age.isnumeric():
    print("invalid age")
    # terminate
    os._exit(0)
    # syt.exit()

if int(age) > 18:
    print(name + " is an Adult")
else:
    print(name + " is aChild")
