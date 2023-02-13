# RATING: 1200⤶
# TAGS: brute force,implementation⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# The Olympic Games have just started and Federico is eager to watch the⤶
# marathon race.⤶
# ⤶
# There will be n athletes, numbered from 1 to n, competing in the marathon, and⤶
# all of them have taken part in 5 important marathons, numbered from 1 to 5, in⤶
# the past. For each 1≤ i≤ n and 1≤ j≤ 5, Federico remembers that athlete i⤶
# ranked r_{i,j}-th in marathon j (e.g., r_{2,4}=3 means that athlete 2 was⤶
# third in marathon 4).⤶
# ⤶
# Federico considers athlete x superior to athlete y if athlete x ranked better⤶
# than athlete y in at least 3 past marathons, i.e., r_{x,j}<r_{y,j} for at⤶
# least 3 distinct values of j.⤶
# ⤶
# Federico believes that an athlete is likely to get the gold medal at the⤶
# Olympics if he is superior to all other athletes.⤶
# ⤶
# Find any athlete who is likely to get the gold medal (that is, an athlete who⤶
# is superior to all other athletes), or determine that there is no such⤶
# athlete.⤶
# ⤶
# Input⤶
# ⤶
# The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test⤶
# cases. Then t test cases follow.⤶
# ⤶
# The first line of each test case contains a single integer n (1≤ n≤ 50 000) —⤶
# the number of athletes.⤶
# ⤶
# Then n lines follow, each describing the ranking positions of one athlete.⤶
# ⤶
# The i-th of these lines contains the 5 integers⤶
# r_{i,1},\,r_{i,2},\,r_{i,3},\,r_{i,4},  r_{i,5} (1≤ r_{i,j}≤ 50 000) — the⤶
# ranking positions of athlete i in the past 5 marathons. It is guaranteed that,⤶
# in each of the 5 past marathons, the n athletes have distinct ranking⤶
# positions, i.e., for each 1≤ j≤ 5, the n values r_{1,j},  r_{2, j},  ...,⤶
# r_{n, j} are distinct.⤶
# ⤶
# It is guaranteed that the sum of n over all test cases does not exceed 50 000.⤶
# ⤶
# Output⤶
# ⤶
# For each test case, print a single integer — the number of an athlete who is⤶
# likely to get the gold medal (that is, an athlete who is superior to all other⤶
# athletes). If there are no such athletes, print -1. If there is more than such⤶
# one athlete, print any of them.⤶
# ⤶
# Example⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 4⤶
# 1⤶
# 50000 1 50000 50000 50000⤶
# 3⤶
# 10 10 20 30 30⤶
# 20 20 30 10 10⤶
# 30 30 10 20 20⤶
# 3⤶
# 1 1 1 1 1⤶
# 2 2 2 2 2⤶
# 3 3 3 3 3⤶
# 6⤶
# 9 5 3 7 1⤶
# 7 4 1 6 8⤶
# 5 6 7 3 2⤶
# 6 7 8 8 6⤶
# 4 2 2 4 5⤶
# 8 3 6 9 4⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 1⤶
# -1⤶
# 1⤶
# 5⤶
# ⤶
# Note⤶
# ⤶
# Explanation of the first test case: There is only one athlete, therefore he is⤶
# superior to everyone else (since there is no one else), and thus he is likely⤶
# to get the gold medal.⤶
# ⤶
# Explanation of the second test case: There are n=3 athletes.⤶
# ⤶
#   * Athlete 1 is superior to athlete 2. Indeed athlete 1 ranks better than⤶
# athlete 2 in the marathons 1, 2 and 3.⤶
#   * Athlete 2 is superior to athlete 3. Indeed athlete 2 ranks better than⤶
# athlete 3 in the marathons 1, 2, 4 and 5.⤶
#   * Athlete 3 is superior to athlete 1. Indeed athlete 3 ranks better than⤶
# athlete 1 in the marathons 3, 4 and 5.⤶
# ⤶
# ⤶
# ⤶
# Explanation of the third test case: There are n=3 athletes.⤶
# ⤶
#   * Athlete 1 is superior to athletes 2 and 3. Since he is superior to all⤶

def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            cnt1 = 0
            for k in range(5):
                if a[i][k] < a[j][k]:
                    cnt1 += 1
            if cnt1 >= 3:
                cnt += 1
        if cnt == n - 1:
            print(i + 1)
            return
    print(-1)

t = int(input())
for i in range(t):
    solve()
