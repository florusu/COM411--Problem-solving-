print("Please choose an option from the menu :\n\n1-Nice message\n2-Area of a rectangle\n3-Area of a triangle\n4-Times table")

option = int(input())

if option == 1:
  print("Today will be a good day !")
elif option == 2:
 print("enter the length of a rectangle:")
 l =int(input())
 print("enter the width of the rectangle:")
 w = int(input())
 area = w*1
 print("The area of a rectangle was {}".format(area))
elif option == 3:
  print("Enter the base of a triangle:")
  base = float(input())
  print("Enter the height of a triangle:")
  height= float(input())
  area =0.5*base*height
  print("The area of this triangle was {:.2f}".format(area))
elif option == 4:
  print("what number would you like to see this table for?")
  n = int(input())

for i in range(1,11,1):
 print("{}x{} = {}".format(n,i,n*i))


else :
 print("There is no such option. Go to specsavers! ")

  