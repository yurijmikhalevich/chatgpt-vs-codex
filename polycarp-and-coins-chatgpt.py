t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    c1 = n // 2
    c2 = n // 2
    if n % 2 == 1:
        c1 += 1
    print(c1, c2)

