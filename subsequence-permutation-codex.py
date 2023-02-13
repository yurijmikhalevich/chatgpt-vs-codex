# RATING: 1200⤶
# TAGS: implementation,sortings⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# A string s of length n, consisting of lowercase letters of the English⤶
# alphabet, is given.⤶
# ⤶
# You must choose some number k between 0 and n. Then, you select k characters⤶
# of s and permute them however you want. In this process, the positions of the⤶
# other n-k characters remain unchanged. You have to perform this operation⤶
# exactly once.⤶
# ⤶
# For example, if s="andrea", you can choose the k=4 characters "a_d_ea" and⤶
# permute them into "d_e_aa" so that after the operation the string becomes⤶
# "dneraa".⤶
# ⤶
# Determine the minimum k so that it is possible to sort s alphabetically (that⤶
# is, after the operation its characters appear in alphabetical order).⤶
# ⤶
# Input⤶
# ⤶
# The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test⤶
# cases. Then t test cases follow.⤶
# ⤶
# The first line of each test case contains one integer n (1 ≤ n ≤ 40) — the⤶
# length of the string.⤶
# ⤶
# The second line of each test case contains the string s. It is guaranteed that⤶
# s contains only lowercase letters of the English alphabet.⤶
# ⤶
# Output⤶
# ⤶
# For each test case, output the minimum k that allows you to obtain a string⤶
# sorted alphabetically, through the operation described above.⤶
# ⤶
# Example⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 4⤶
# 3⤶
# lol⤶
# 10⤶
# codeforces⤶
# 5⤶
# aaaaa⤶
# 4⤶
# dcba⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 2⤶
# 6⤶
# 0⤶
# 4⤶
# ⤶
# Note⤶
# ⤶
# In the first test case, we can choose the k=2 characters "_ol" and rearrange⤶
# them as "_lo" (so the resulting string is "llo"). It is not possible to sort⤶
# the string choosing strictly less than 2 characters.⤶
# ⤶
# In the second test case, one possible way to sort s is to consider the k=6⤶
# characters "_o__force_" and rearrange them as "_c__efoor_" (so the resulting⤶
# string is "ccdeefoors"). One can show that it is not possible to sort the⤶
# string choosing strictly less than 6 characters.⤶
# ⤶
# In the third test case, string s is already sorted (so we can choose k=0⤶
# characters).⤶
# ⤶
# In the fourth test case, we can choose all k=4 characters "dcba" and reverse⤶
# the whole string (so the resulting string is "abcd").⤶

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    k = 0
    for i in range(n - 1, 0, -1):
        if s[i] < s[i - 1]:
            k = i
            break
    print(k)

# Time: 31 ms, memory: 0 KB
