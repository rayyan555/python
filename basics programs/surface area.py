import math

def calculate_volume(radius, height):
    volume = math.pi * radius * radius * height
    return volume

def calculate_surface_area(radius, height):
    surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
    return surface_area

# Taking input from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculating the volume and surface area
volume = calculate_volume(radius, height)
surface_area = calculate_surface_area(radius, height)

# Printing the results
print("Volume of the cylinder:", volume)
print("Surface area of the cylinder:", surface_area)
