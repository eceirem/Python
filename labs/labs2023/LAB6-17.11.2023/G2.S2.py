import ast
def sumRationalNums(list):
    numerator = 0
    denominator = 0
    rational1 = list[0]
    rational2 = list[1]
    denominator = rational1[1]*rational2[1]
    numerator = rational1[0]*rational2[1] + rational2[0]*rational1[1]
    return int(numerator/denominator)

list = input()
list = ast.literal_eval(list)

sumofrational = sumRationalNums(list)

print(sumofrational)