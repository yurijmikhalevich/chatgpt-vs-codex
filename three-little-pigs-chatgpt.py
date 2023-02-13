MOD = 10**9 + 7

def solve(n, x):
    if x > 3 * n:
        return 0
    if x <= n:
        return pow(3, n - x + 1, MOD)
    return pow(2, n - (x - 1) // 3, MOD)

n, q = map(int, input().split())
for _ in range(q):
    x = int(input().strip())
    print(solve(n, x) % MOD)
