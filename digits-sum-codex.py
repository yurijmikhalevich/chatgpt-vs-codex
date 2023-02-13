# RATING: 1200⤶
# TAGS: *special⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# Let's define S(x) to be the sum of digits of number x written in decimal⤶
# system. For example, S(5) = 5, S(10) = 1, S(322) = 7.⤶
# ⤶
# We will call an integer x interesting if S(x + 1) < S(x). In each test you⤶
# will be given one integer n. Your task is to calculate the number of integers⤶
# x such that 1 ≤ x ≤ n and x is interesting.⤶
# ⤶
# Input⤶
# ⤶
# The first line contains one integer t (1 ≤ t ≤ 1000) — number of test cases.⤶
# ⤶
# Then t lines follow, the i-th line contains one integer n (1 ≤ n ≤ 10^9) for⤶
# the i-th test case.⤶
# ⤶
# Output⤶
# ⤶
# Print t integers, the i-th should be the answer for the i-th test case.⤶
# ⤶
# Example⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 5⤶
# 1⤶
# 9⤶
# 10⤶
# 34⤶
# 880055535⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 0⤶
# 1⤶
# 1⤶
# 3⤶
# 88005553⤶
# ⤶
# Note⤶
# ⤶
# The first interesting number is equal to 9.⤶

def digits_sum(x):
    return sum(int(c) for c in str(x))

def interesting(n):
    return sum(digits_sum(x + 1) < digits_sum(x) for x in range(1, n + 1))

def main():
    for _ in range(int(input())):
        print(interesting(int(input())))

main()
