#Calculating area of given shapes
import math

def calculate_area():
    print("Choose the given geometric shapes")
    print("1. Rectangle")
    print("2. Square")
    print("3. Trinagle")
    print("4. Circle")
    
    choice = int(input("Enter the corresponding number with respect to geometric shape i.e (1-4) "))

    if choice == 1:
        
        length = float(input("Enter the length of rectangle - "))
        breath = float(input("Enter the breath of rectangle - "))
        area = length*breath
        print(f"The area of Rectangle with length {length:.4f:.4f} and breath {breath:.4f} is - {area:.4f}.")
        
    elif choice == 2:
        
        side = float(input("Enter the side of square - "))
        area = side**2 # area = side*side
        print(f"The area of Square with side {side:.4f} is - {area:.4f}.")
        
    elif choice == 3:

        base = float(input("Enter the base of triangle - "))
        height = float(input("Enter the height of triangle - "))
        area = 0.5*base*height
        print(f"The area of Traingle with base {base:.4f} and height {height:.4f} is - {area:.4f}.")
        
    elif choice == 4:
        
        radius = float(input("Enter the radius of circle - "))
        area = 2*radius*math.pi
        print(f"The area of Circle with radius {radius:.4f} is - {area:.4f}.")
        
    else:
            print("Your input is valid")

#Calling the geometric shape calculation function
calculate_area()