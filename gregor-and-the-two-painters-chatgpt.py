def DFS(x, y):
    vis[x][y] = 1
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and a[nx] + b[ny] <= x_:
            DFS(nx, ny)

n, m, x_ = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
vis = [[0] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j] and a[i] + b[j] <= x_:
            DFS(i, j)
            ans += 1
print(ans)

