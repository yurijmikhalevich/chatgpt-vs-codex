# RATING: 1200⤶
# TAGS: combinatorics,dp,math⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# Three little pigs from all over the world are meeting for a convention! Every⤶
# minute, a triple of 3 new pigs arrives on the convention floor. After the n-th⤶
# minute, the convention ends.⤶
# ⤶
# The big bad wolf has learned about this convention, and he has an attack plan.⤶
# At some minute in the convention, he will arrive and eat exactly x pigs. Then⤶
# he will get away.⤶
# ⤶
# The wolf wants Gregor to help him figure out the number of possible attack⤶
# plans that involve eating exactly x pigs for various values of x (1 ≤ x ≤ 3n).⤶
# Two attack plans are considered different, if they occur at different times or⤶
# if the sets of little pigs to eat are different.⤶
# ⤶
# Note that all queries are independent, that is, the wolf does not eat the⤶
# little pigs, he only makes plans!⤶
# ⤶
# Input⤶
# ⤶
# The first line of input contains two integers n and q (1 ≤ n ≤ 10^6, 1 ≤ q ≤⤶
# 2⋅ 10^5), the number of minutes the convention lasts and the number of queries⤶
# the wolf asks.⤶
# ⤶
# Each of the next q lines contains a single integer x_i (1 ≤ x_i ≤ 3n), the⤶
# number of pigs the wolf will eat in the i-th query.⤶
# ⤶
# Output⤶
# ⤶
# You should print q lines, with line i representing the number of attack plans⤶
# if the wolf wants to eat x_i pigs. Since each query answer can be large,⤶
# output each answer modulo 10^9+7.⤶
# ⤶
# Examples⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 2 3⤶
# 1⤶
# 5⤶
# 6⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 9⤶
# 6⤶
# 1⤶
# ⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 5 4⤶
# 2⤶
# 4⤶
# 6⤶
# 8⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 225⤶
# 2001⤶
# 6014⤶
# 6939⤶
# ⤶
# Note⤶
# ⤶
# In the example test, n=2. Thus, there are 3 pigs at minute 1, and 6 pigs at⤶
# minute 2. There are three queries: x=1, x=5, and x=6.⤶
# ⤶
# If the wolf wants to eat 1 pig, he can do so in 3+6=9 possible attack plans,⤶
# depending on whether he arrives at minute 1 or 2.⤶
# ⤶
# If the wolf wants to eat 5 pigs, the wolf cannot arrive at minute 1, since⤶
# there aren't enough pigs at that time. Therefore, the wolf has to arrive at⤶
# minute 2, and there are 6 possible attack plans.⤶
# ⤶
# If the wolf wants to eat 6 pigs, his only plan is to arrive at the end of the⤶
# convention and devour everybody.⤶
# ⤶
# Remember to output your answers modulo 10^9+7!⤶

import sys
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    MOD = 10**9 + 7
    dp = [0] * (3 * n + 1)
    dp[0] = 1
    for i in range(1, 3 * n + 1):
        dp[i] = dp[i - 1]
        if i >= 3:
            dp[i] += dp[i - 3]
        dp[i] %= MOD
    for _ in range(q):
        x = int(input())
        print(dp[x])

main()
