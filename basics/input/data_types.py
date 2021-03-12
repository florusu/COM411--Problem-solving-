print("what is your name human?")
name = input()
print("how old are you?")
age = int(input())
print("how tall are you?")
height = float(input())
print("how much do you weigh?")
weight = int(input())

bmi = weight / height*2
print("{} you are {} old and your bmi is {}.".format(name,age,bmi))