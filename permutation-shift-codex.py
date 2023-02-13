# RATING: 1200⤶
# TAGS: binary search,data structures⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# An identity permutation of length n is an array [1, 2, 3, ..., n].⤶
# ⤶
# We performed the following operations to an identity permutation of length n:⤶
# ⤶
#   * firstly, we cyclically shifted it to the right by k positions, where k is⤶
# unknown to you (the only thing you know is that 0 ≤ k ≤ n - 1). When an array⤶
# is cyclically shifted to the right by k positions, the resulting array is⤶
# formed by taking k last elements of the original array (without changing their⤶
# relative order), and then appending n - k first elements to the right of them⤶
# (without changing relative order of the first n - k elements as well). For⤶
# example, if we cyclically shift the identity permutation of length 6 by 2⤶
# positions, we get the array [5, 6, 1, 2, 3, 4];⤶
#   * secondly, we performed the following operation at most m times: pick any⤶
# two elements of the array and swap them.⤶
# ⤶
# ⤶
# ⤶
# You are given the values of n and m, and the resulting array. Your task is to⤶
# find all possible values of k in the cyclic shift operation.⤶
# ⤶
# Input⤶
# ⤶
# The first line contains one integer t (1 ≤ t ≤ 10^5) — the number of test⤶
# cases.⤶
# ⤶
# Each test case consists of two lines. The first line contains two integers n⤶
# and m (3 ≤ n ≤ 3 ⋅ 10^5; 0 ≤ m ≤ n/3).⤶
# ⤶
# The second line contains n integers p_1, p_2, ..., p_n (1 ≤ p_i ≤ n, each⤶
# integer from 1 to n appears in this sequence exactly once) — the resulting⤶
# array.⤶
# ⤶
# The sum of n over all test cases does not exceed 3 ⋅ 10^5.⤶
# ⤶
# Output⤶
# ⤶
# For each test case, print the answer in the following way:⤶
# ⤶
#   * firstly, print one integer r (0 ≤ r ≤ n) — the number of possible values⤶
# of k for the cyclic shift operation;⤶
#   * secondly, print r integers k_1, k_2, ..., k_r (0 ≤ k_i ≤ n - 1) — all⤶
# possible values of k in increasing order.⤶
# ⤶
# Example⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 4⤶
# 4 1⤶
# 2 3 1 4⤶
# 3 1⤶
# 1 2 3⤶
# 3 1⤶
# 3 2 1⤶
# 6 0⤶
# 1 2 3 4 6 5⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 1 3⤶
# 1 0⤶
# 3 0 1 2⤶
# 0⤶
# ⤶
# Note⤶
# ⤶
# Consider the example:⤶
# ⤶
#   * in the first test case, the only possible value for the cyclic shift is 3.⤶
# If we shift [1, 2, 3, 4] by 3 positions, we get [2, 3, 4, 1]. Then we can swap⤶
# the 3-rd and the 4-th elements to get the array [2, 3, 1, 4];⤶
#   * in the second test case, the only possible value for the cyclic shift is⤶
# 0. If we shift [1, 2, 3] by 0 positions, we get [1, 2, 3]. Then we don't⤶
# change the array at all (we stated that we made at most 1 swap), so the⤶
# resulting array stays [1, 2, 3];⤶
#   * in the third test case, all values from 0 to 2 are possible for the cyclic⤶
# shift:⤶
#     * if we shift [1, 2, 3] by 0 positions, we get [1, 2, 3]. Then we can swap⤶
# the 1-st and the 3-rd elements to get [3, 2, 1];⤶
#     * if we shift [1, 2, 3] by 1 position, we get [3, 1, 2]. Then we can swap⤶
# the 2-nd and the 3-rd elements to get [3, 2, 1];⤶
#     * if we shift [1, 2, 3] by 2 positions, we get [2, 3, 1]. Then we can swap⤶
# the 1-st and the 2-nd elements to get [3, 2, 1];⤶
#   * in the fourth test case, we stated that we didn't do any swaps after the⤶
# cyclic shift, but no value of cyclic shift could produce the array [1, 2, 3,⤶
# 4, 6, 5].⤶

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    if m == 0:
        print(1, p.index(1))
        return
    if m == n // 3:
        print(0)
        return
    ans = []
    for i in range(n):
        if p[i] == 1:
            break
    for j in range(n):
        if p[(i + j) % n] != j + 1:
            break
    else:
        ans.append(i)
    for j in range(n):
        if p[(i - j) % n] != j + 1:
            break
    else:
        ans.append((i - 1) % n)
    print(len(ans), *ans)

t = int(input())
for _ in range(t):
    solve()
