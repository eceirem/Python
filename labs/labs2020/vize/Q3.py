x,y = 0,0
origin = (0,0)

inputs = input()
while inputs != "-1":
    move = inputs.split()[0]
    dis = int(inputs.split()[1])

    if move == "left":
        x -= dis
    elif move == "right":
        x += dis
    elif move == "up":
        y += dis
    elif move == "down":
        y -= dis
    else:
        continue
    inputs = input()

distance = ((origin[0]-x)**2 + (origin[1]-y)**2)**0.5
print(distance)