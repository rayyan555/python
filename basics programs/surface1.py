radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
pi = 3.14

volume = pi * radius * radius * height
surface_area = ((2 * pi * radius) * height) + ((pi * radius ** 2) * 2)

print("Volume of the cylinder:", volume)
print("Surface area of the cylinder:", surface_area)
