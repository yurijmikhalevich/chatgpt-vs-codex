from collections import Counter

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    c = Counter(s)
    print(min(len(s)//2, len(c)))

