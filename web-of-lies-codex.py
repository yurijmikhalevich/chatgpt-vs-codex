# RATING: 1200⤶
# TAGS: brute force,math⤶
# LANGUAGE IS python3⤶
# CORRECT SOLUTION⤶
# When you play the game of thrones, you win, or you die. There is no middle⤶
# ground.⤶
# ⤶
# Cersei Lannister, A Game of Thrones by George R. R. Martin⤶
# ⤶
# There are n nobles, numbered from 1 to n. Noble i has a power of i. There are⤶
# also m "friendships". A friendship between nobles a and b is always mutual.⤶
# ⤶
# A noble is defined to be vulnerable if both of the following conditions are⤶
# satisfied:⤶
# ⤶
#   * the noble has at least one friend, and⤶
#   * all of that noble's friends have a higher power.⤶
# ⤶
# ⤶
# ⤶
# You will have to process the following three types of queries.⤶
# ⤶
#   1. Add a friendship between nobles u and v.⤶
#   2. Remove a friendship between nobles u and v.⤶
#   3. Calculate the answer to the following process.⤶
# ⤶
# ⤶
# ⤶
# The process: all vulnerable nobles are simultaneously killed, and all their⤶
# friendships end. Then, it is possible that new nobles become vulnerable. The⤶
# process repeats itself until no nobles are vulnerable. It can be proven that⤶
# the process will end in finite time. After the process is complete, you need⤶
# to calculate the number of remaining nobles.⤶
# ⤶
# Note that the results of the process are not carried over between queries,⤶
# that is, every process starts with all nobles being alive!⤶
# ⤶
# Input⤶
# ⤶
# The first line contains the integers n and m (1 ≤ n ≤ 2⋅ 10^5, 0 ≤ m ≤ 2⋅⤶
# 10^5) — the number of nobles and number of original friendships respectively.⤶
# ⤶
# The next m lines each contain the integers u and v (1 ≤ u,v ≤ n, u ≠ v),⤶
# describing a friendship. No friendship is listed twice.⤶
# ⤶
# The next line contains the integer q (1 ≤ q ≤ 2⋅ {10}^{5}) — the number of⤶
# queries.⤶
# ⤶
# The next q lines contain the queries themselves, each query has one of the⤶
# following three formats.⤶
# ⤶
#   * 1 u v (1 ≤ u,v ≤ n, u ≠ v) — add a friendship between u and v. It is⤶
# guaranteed that u and v are not friends at this moment.⤶
#   * 2 u v (1 ≤ u,v ≤ n, u ≠ v) — remove a friendship between u and v. It is⤶
# guaranteed that u and v are friends at this moment.⤶
#   * 3 — print the answer to the process described in the statement.⤶
# ⤶
# Output⤶
# ⤶
# For each type 3 query print one integer to a new line. It is guaranteed that⤶
# there will be at least one type 3 query.⤶
# ⤶
# Examples⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 4 3⤶
# 2 1⤶
# 1 3⤶
# 3 4⤶
# 4⤶
# 3⤶
# 1 2 3⤶
# 2 3 1⤶
# 3⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 2⤶
# 1⤶
# ⤶
# ⤶
# Input⤶
# ⤶
# ⤶
# 4 3⤶
# 2 3⤶
# 3 4⤶
# 4 1⤶
# 1⤶
# 3⤶
# ⤶
# ⤶
# Output⤶
# ⤶
# ⤶
# 1⤶
# ⤶
# Note⤶
# ⤶
# Consider the first example. In the first type 3 query, we have the diagram⤶
# below.⤶
# ⤶
# In the first round of the process, noble 1 is weaker than all of his friends⤶
# (2 and 3), and is thus killed. No other noble is vulnerable in round 1. In⤶
# round 2, noble 3 is weaker than his only friend, noble 4, and is therefore⤶
# killed. At this point, the process ends, and the answer is 2.⤶
# ⤶
# <image>⤶
# ⤶
# In the second type 3 query, the only surviving noble is 4.⤶
# ⤶
# The second example consists of only one type 3 query. In the first round, two⤶
# nobles are killed, and in the second round, one noble is killed. The final⤶
# answer is 1, since only one noble survives.⤶
# ⤶
# <image>⤶

import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i] )
        return self.parent[i]

    def union(self, i, j):
        x, y = self.find(i), self.find(j)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        self.parent[x] = y
        self.size[y] += self.size[x]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.num_sets -= 1

    def is_same_set(self, i, j):
        return self.find(i) == self.find(j)

    def num_disjoint_sets(self):
        return self.num_sets

    def size_of_set(self, i):
        return self.size[self.find(i)]

def main():
    n, m = map(int, sys.stdin.readline().split())
    uf = UnionFind(n)
    friends = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        friends[u].add(v)
        friends[v].add(u)
        uf.union(u, v)
    q = int(sys.stdin.readline())
    for _ in range(q):
        line = sys.stdin.readline().split()
        if line[0] == '1':
            u, v = map(int, line[1:])
            u -= 1
            v -= 1
            friends[u].add(v)
            friends[v].add(u)
            uf.union(u, v)
        elif line[0] == '2':
            u, v = map(int, line[1:])
            u -= 1
            v -= 1
            friends[u].remove(v)
            friends[v].remove(u)
            uf.union(u, v)
        else:
            print(uf.num_disjoint_sets())

if __name__ == '__main__':
    main()
