import math
print("==================")
print("Area Calculator 📐")
print("==================")
print("")

#Ask the user what shape to pick
print("Choose one of the following shapes: ")
print("1) Square")
print("2) Rectangle")
print("3) Triangle")
print("4) Circle")
print("5) Quit")
print("")

#User enters the one of the options
shape = int(input("Pick using the numbers that are at the side of the shape: "))
print("")

#Loops to make give the user the chance of using the correct number in case of giving an option that is not in the list
while shape >= 0:
    if shape == 5:
        print("You quit the application")
        break

    elif shape == 1:
        side = int(input("Please enter the side of the Square: "))
        area = side ** 2
        print("")
        print("The side is: " + str(side))
        print("The area is: " + str(area))
        break

    elif shape == 2:
        lengthT = int(input("Please enter the length of the Rectangle: "))
        widthT = int(input("Please enter the width of the Rectangle: "))
        area = lengthT * widthT
        print("")
        print("The length is: " + str(lengthT))
        print("The width is: " + str(widthT))
        print("The area is: " + str(area))
        break

    elif shape == 3:
        height = int(input("Please enter the height of the Triangle: "))
        base = int(input("Please enter the base of the Triangle: "))
        area = (height * base)//2
        print("")
        print("The height is: " + str(height))
        print("The base is: " + str(base))
        print("The area is: " + str(area))
        break

    elif shape == 4:
        radius = int(input("Please enter the radius of the Circle: "))
        area = math.pi * (radius**2)
        print("")
        print("The radius is: " + str(radius))
        print("The area is: " + str(area))
        break

    else:
        print("Please enter a number from 1 to 5 to pick a shape or quit the application..")
        shape = int(input("Pick using the numbers that are at the side of the shape: "))
        print("")
