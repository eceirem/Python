num1 = input()
num2 = input()
num3 = input()

if num1.isdigit() and num2.isdigit() and num3.isdigit():
    if num2 < num1 < num3 or num3 < num1 <num2:
        print("True")
    else:
        print("False")
else:
    print("False")