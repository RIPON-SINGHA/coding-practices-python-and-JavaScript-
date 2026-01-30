# chcking the longest increasing streak in a given list of integer
# [1,2,3,1,2.3,4,5,6,1,2,3,4,5,6,7,8,9] => 9

List = [1,2,3,1,2,3,4,5,0,2,1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6]
currStreak = 1
bestStreak = 1

for i in range(1, len(List)):
    if List[i] > List[i-1]:
        currStreak += 1
    else:
        bestStreak = max(currStreak, bestStreak)
        currStreak = 1

bestStreak = max(currStreak, bestStreak)
print(f"The longest increasing streak is: {bestStreak}")