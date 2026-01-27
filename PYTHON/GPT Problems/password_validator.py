# creating a simple system that will check the strenght of a password given by user

# rule 1: Must be 8 characters
# rule 2: At least one digit of number
# rule 3: At least one uppercase letter
# rule 4: No crashes Allowed in code

# BASIC LEVEL IMPLEMENTATION:
# def haveDigit(p):
#     for i in p:
#         if i in "1234567890":
#             return True
#     return False


# def isUpper(p):
#     for i in p:
#         if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#             return True
#     return False


# while True:
#     password = input("Enter your password: ")

#     if len(password) < 8:
#         print("password must be atleast 8 characters long")
#         continue
#     elif haveDigit(password) == False:
#         print("Password must have at least one digit")
#         continue
#     elif isUpper(password) == False:
#         print("Password must have one upper case letter")
#         continue
#     else:
#         print("Password accepted.")
#         break



#INTERMEDIATE LEVEN IMPLEMENTATION
while True:
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password must be 8 character long")
        continue
        
    hasDigit = False
    hasUpper = False

    for ch in password:
        if ch.isdigit():
            hasDigit = True
        elif ch.isupper():
            hasUpper = True
    

    if not hasDigit:
        print("Password must contain at least one digit")
    elif not hasUpper:
        print("Password must contain at least one upper case letter")
    else:
        print("Password aceepted")
        break