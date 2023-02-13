def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    def f(x):
        b = [ai ^ x for ai in a]
        b.sort()
        res = float('inf')
        for i in range(n - 1):
            res = min(res, b[i + 1] - b[i])
        return res

    for i in range(2**k):
        print(f(i), end=' ')

if __name__ == '__main__':
    main()

