# LEFT ANGLED INVERTED TRIANGLE
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


for i in range(5, 0, -1):
    print("*" * i, sep="")
    
    
    
    
    
    
    
    
# RIGHT ANGLED TRIANGLE    
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


for i in range(1, 6):
    print("*" * i, sep="")







# LEFT ANGLED TRIANGLE
for i in range(1, 5+1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()






# THESE BOTH ARE FOR RIGHT ANGLED INVERTED TRIANGLE
for i in range(1, 6):
    for j in range(6, i, -1):
        print("*", end="")
    print()
    for k in range(i):
        print(" ", end="")
        
        

        
for i in range(1, 6):
    for j in range(i - 1):
        print(" ", end="")
    for k in range(6 - i):
        print("*", end="")
    print()
        
        
        
        
        
        
        
# SQUARE        
for i in range(1,6):
    for j in range(5):
        print("*", end="")
    print()
        


#DIAMOND PATTERN 
len = 9
mid = len // 2 

for i in range(0, mid + 1):
    for j in range(mid - i):
        print(" ", end = "")
    for k in range(i + (i + 1)):
        print("*", end = "")
    print()

for i in range(mid + 1, len):
    for j in range(i - mid):
        print(" ", end = "")
    for k in range(len - 2*(i - mid)):
        print("*", end = "")

    print()






# MORE PATTERNS TO COME LATER