def sum_upto(n):
    ans = 0
    for i in range(1, n+1):
        ans = ans + i
    return ans

n = int(input("What will be the range? "))
result = sum_upto(n)
print(result)


# ans = 0
# for i in range (1,6):
#     ans = ans + i

# print(ans)