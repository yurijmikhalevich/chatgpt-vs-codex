# RATING: 1200⤶
# TAGS: dfs and similar,graphs,trees⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# Two painters, Amin and Benj, are repainting Gregor's living room ceiling! The⤶
# ceiling can be modeled as an n × m grid.⤶
# ⤶
# For each i between 1 and n, inclusive, painter Amin applies a_i layers of⤶
# paint to the entire i-th row. For each j between 1 and m, inclusive, painter⤶
# Benj applies b_j layers of paint to the entire j-th column. Therefore, the⤶
# cell (i,j) ends up with a_i+b_j layers of paint.⤶
# ⤶
# Gregor considers the cell (i,j) to be badly painted if a_i+b_j ≤ x. Define a⤶
# badly painted region to be a maximal connected component of badly painted⤶
# cells, i. e. a connected component of badly painted cells such that all⤶
# adjacent to the component cells are not badly painted. Two cells are⤶
# considered adjacent if they share a side.⤶
# ⤶
# Gregor is appalled by the state of the finished ceiling, and wants to know the⤶
# number of badly painted regions.⤶
# ⤶
# Input⤶
# ⤶
# The first line contains three integers n, m and x (1 ≤ n,m ≤ 2⋅ 10^5, 1 ≤ x ≤⤶
# 2⋅ 10^5) — the dimensions of Gregor's ceiling, and the maximum number of paint⤶
# layers in a badly painted cell.⤶
# ⤶
# The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 2⋅ 10^5), the⤶
# number of paint layers Amin applies to each row.⤶
# ⤶
# The third line contains m integers b_1, b_2, ..., b_m (1 ≤ b_j ≤ 2⋅ 10^5), the⤶
# number of paint layers Benj applies to each column.⤶
# ⤶
# Output⤶
# ⤶
# Print a single integer, the number of badly painted regions.⤶
# ⤶
# Examples⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 3 4 11⤶
# 9 8 5⤶
# 10 6 7 2⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 2⤶
# ⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 3 4 12⤶
# 9 8 5⤶
# 10 6 7 2⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 1⤶
# ⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 3 3 2⤶
# 1 2 1⤶
# 1 2 1⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 4⤶
# ⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 5 23 6⤶
# 1 4 3 5 2⤶
# 2 3 1 6 1 5 5 6 1 3 2 6 2 3 1 6 1 4 1 6 1 5 5⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 6⤶
# ⤶
# Note⤶
# ⤶
# The diagram below represents the first example. The numbers to the left of⤶
# each row represent the list a, and the numbers above each column represent the⤶
# list b. The numbers inside each cell represent the number of paint layers in⤶
# that cell.⤶
# ⤶
# The colored cells correspond to badly painted cells. The red and blue cells⤶
# respectively form 2 badly painted regions.⤶
# ⤶
# <image>⤶

import sys
from collections import deque

def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    grid = [[a[i] + b[j] for j in range(m)] for i in range(n)]
    visited = [[False for j in range(m)] for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] <= x:
                count += 1
                visited[i][j] = True
                q = deque([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
                while q:
                    i, j = q.popleft()
                    if 0 <= i < n and 0 <= j < m and not visited[i][j] and grid[i][j] <= x:
                        visited[i][j] = True
                        q.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
    print(count)

if __name__ == '__main__':
    main()

# This solution was
# submitted and prepared by
# the following authors:
#   * 0x0000000000000
