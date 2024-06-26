str1 = "abcdegasbfabafdxx"
str2 = "xazcfdgbazgbgadaa"
same_str = " "
for i in str1:
    if i in str2 and (i not in same_str):
        same_str += i


print("the same elements are: ", same_str)