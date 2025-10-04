import os
os.system('cls')

number = input("enter numbers separated by space: ")

#convert input user from string to integer list
number = list(map(int, number.split()))

#sort nuber via .sort function
number.sort()

print("your sorted list from least to greatest: " )
print(number)

