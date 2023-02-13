# RATING: 1200⤶
# TAGS:⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# You are given an array a consisting of n distinct elements and an integer k.⤶
# Each element in the array is a non-negative integer not exceeding 2^k-1.⤶
# ⤶
# Let's define the XOR distance for a number x as the value of⤶
# ⤶
# $$$f(x) = min_{i = 1}^{n} min_{j = i + 1}^{n} |(a_i ⊕ x) - (a_j ⊕ x)|,$$$⤶
# ⤶
# where ⊕ denotes [the bitwise XOR⤶
# operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).⤶
# ⤶
# For every integer x from 0 to 2^k-1, you have to calculate f(x).⤶
# ⤶
# Input⤶
# ⤶
# The first line contains two integers n and k (1 ≤ k ≤ 19; 2 ≤ n ≤ 2^k).⤶
# ⤶
# The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ 2^k-1). All⤶
# these integers are distinct.⤶
# ⤶
# Output⤶
# ⤶
# Print 2^k integers. The i-th of them should be equal to f(i-1).⤶
# ⤶
# Examples⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 3 3⤶
# 6 0 3⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 3 1 1 2 2 1 1 3⤶
# ⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 3 4⤶
# 13 4 2⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 2 2 6 6 3 1 2 2 2 2 1 3 6 6 2 2⤶
# ⤶
# Note⤶
# ⤶
# Consider the first example:⤶
# ⤶
#   * for x = 0, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [6, 0, 3], and the minimum absolute difference of two elements⤶
# is 3;⤶
#   * for x = 1, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [7, 1, 2], and the minimum absolute difference of two elements⤶
# is 1;⤶
#   * for x = 2, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [4, 2, 1], and the minimum absolute difference of two elements⤶
# is 1;⤶
#   * for x = 3, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [5, 3, 0], and the minimum absolute difference of two elements⤶
# is 2;⤶
#   * for x = 4, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [2, 4, 7], and the minimum absolute difference of two elements⤶
# is 2;⤶
#   * for x = 5, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [3, 5, 6], and the minimum absolute difference of two elements⤶
# is 1;⤶
#   * for x = 6, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [0, 6, 5], and the minimum absolute difference of two elements⤶
# is 1;⤶
#   * for x = 7, if we apply bitwise XOR to the elements of the array with x, we⤶
# get the array [1, 7, 4], and the minimum absolute difference of two elements⤶
# is 3.⤶

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = [0] * (1 << k)
for i in range(1 << k):
    for j in range(n):
        for l in range(j + 1, n):
            ans[i] = max(ans[i], abs((a[j] ^ i) - (a[l] ^ i)))
print(*ans)

