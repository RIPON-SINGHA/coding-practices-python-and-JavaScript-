# addition of two largest integer in a list of integer

num_list = list(map(int, input("Enter your numbers: ").split()))

max1 = float('-inf')
max2 = float('-inf')

for num in num_list:
    if num > max1:
        max2 = max1
        max1 = num
    elif num < max1 and num > max2:
        max2 = num

print(max1 + max2)
