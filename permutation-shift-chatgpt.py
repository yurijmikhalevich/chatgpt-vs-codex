def main():
    t = int(input().strip())
    for _ in range(t):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        pos = {}
        for i in range(n):
            pos[a[i]] = i
        k = pos[1]
        r = 0
        for i in range(2, n+1):
            r += (pos[i] - k + n) % n
            k = pos[i]
        r += n - ((n - r) // 2) * 2
        r = n - r
        print(r, end=' ')
        for i in range(r):
            print(i, end=' ')
        print()

if __name__ == '__main__':
    main()

