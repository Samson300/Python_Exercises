# Makes a box with demensions you put in
count = 1

width_input = int(input("Width of box? "))
height_input = int(input("Height of box? "))

wall = "*"

while count <= height_input:
    if count == 1 or count == height_input:
        print(wall * (width_input))
        count += 1
    else:
        print(wall + (" " * (width_input -2)) + wall)
        count += 1