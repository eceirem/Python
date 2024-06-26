total_colony = 0
total_newborn = 0

colony = int(input("Enter the number of does in the rabbit colony(-1 to end): "))

while colony > -1:
    total_colony += colony
    newborn = int(input("Number of baby rabbits born in the past month: "))
    total_newborn += newborn
    print("On average", newborn/colony, "baby rabbits were born for each doe.")
    colony = int(input("Enter the number of does in the rabbit colony(-1 to end): "))
    if colony == -1:
        print(total_newborn/total_colony)