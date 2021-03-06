print("what is your name?")
n = input()
print("do you have a dog ?(types true or false)")
dog = bool(input())
#bool is boolean datatype only stores true or false 

if len(n)>9:
  # and/or 
  print("you have a very loooong name!")
  print("your name contains {}letters".format(len(n)))
elif len(n) > 6:
  print("your name is a bit long , consider a nickname")

elif len(n)<3:
  print("your name is very short")
else:
  print("your name is quite ok")


print("this is the end of the program ")
