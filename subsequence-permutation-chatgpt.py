def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        k = 0
        for i in range(n - 1):
            if s[i] > s[i + 1]:
                k = i + 1
                break
        print(k)

if __name__ == '__main__':
    main()

