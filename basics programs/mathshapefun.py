import math

def sphere(radius, pi=math.pi):
    surface_area = 4 * pi * radius**2
    volume = (4/3) * pi * radius**3
    return surface_area, volume

def cylinder(radius, height, pi=math.pi):
    surface_area = 2 * pi * radius**2 + 2 * pi * radius * height
    volume = pi * radius**2 * height
    return surface_area, volume

def cone(radius, height, pi=math.pi):
    surface_area = pi * radius*2 + pi * radius * math.sqrt(radius2 + height*2)
    volume = (1/3) * pi * radius**2 * height
    return surface_area, volume

def rectangular_prism(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)
    volume = length * width * height
    return surface_area, volume

def triangular_prism(base, height, length):
    surface_area = (base * height) + (length * base) + (length * height) + (2 * math.sqrt((length*2) + (height*2))) 
    volume = (1/2) * base * height * length
    return surface_area, volume

# Get user input for shape parameters
shape = input("Enter the name of the shape (sphere, cylinder, cone, rectangular prism, triangular prism): ")

if shape == "sphere":
    radius = float(input("Enter the radius of the sphere: "))
    surface_area, volume = sphere(radius)
    print("Sphere Surface Area:", surface_area)
    print("Sphere Volume:", volume)
elif shape == "cylinder":
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    surface_area, volume = cylinder(radius, height)
    print("Cylinder Surface Area:", surface_area)
    print("Cylinder Volume:", volume)
elif shape == "cone":
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    surface_area, volume = cone(radius, height)
    print("Cone Surface Area:", surface_area)
    print("Cone Volume:", volume)
elif shape == "rectangular prism":
    length = float(input("Enter the length of the rectangular prism: "))
    width = float(input("Enter the width of the rectangular prism: "))
    height = float(input("Enter the height of the rectangular prism: "))
    surface_area, volume = rectangular_prism(length, width, height)
    print("Rectangular Prism Surface Area:", surface_area)
    print("Rectangular Prism Volume:", volume)
elif shape == "triangular prism":
    base = float(input("Enter the base of the triangular prism: "))
    height = float(input("Enter the height of the triangular prism: "))
    length = float(input("Enter the length of the triangular prism: "))
    surface_area, volume = triangular_prism(base, height, length)
    print("Triangular Prism Surface Area:", surface_area)
    print("Triangular Prism Volume:", volume)
else:
    print("Invalid shape entered!")
