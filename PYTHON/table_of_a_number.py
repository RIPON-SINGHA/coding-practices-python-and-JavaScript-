def main():
    n = int(input("Enter a number: ")) #5
    table(n)


def table(num):
    if(num == 0):
        print("Enter a valid number for multiplication")
    else:
        for i in range(1, 10+1):
            print(num * i)
    
main()
