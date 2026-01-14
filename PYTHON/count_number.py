# def main():
#     number = int(input("Enter your number: "))
#     result = count_num(number)
#     print(f"the lenghh of the number is {result}")

# def count_num(n):
#     if n == 0:
#         return 1
#     count = 0
#     temp_num = abs(n)

#     while temp_num > 0:
#         count += 1
#         temp_num //= 10
#     return count
        


# main()





def main():
    number = int(input("Enter your number: "))
    result = count_digit(number)
    print(f"The lenght of your number is {result}")


def count_digit(n):
    if n == 0:
        return 1
    
    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10

    return count


main()