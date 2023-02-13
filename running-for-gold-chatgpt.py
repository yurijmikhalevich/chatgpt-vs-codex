def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        ranks = []
        for i in range(n):
            ranks.append(list(map(int, input().strip().split())))
        superior = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                cnt = 0
                for k in range(5):
                    if ranks[i - 1][k] < ranks[j - 1][k]:
                        cnt += 1
                if cnt >= 3:
                    superior[j] += 1
        res = -1
        for i in range(1, n + 1):
            if superior[i] == 0:
                if res == -1:
                    res = i
                else:
                    res = -1
                    break
        print(res)

if __name__ == '__main__':
    main()

