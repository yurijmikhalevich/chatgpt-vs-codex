from collections import defaultdict

def solve(n, m, q, friends, queries):
    def is_vulnerable(i):
        return i in all_nobles and len(friends[i]) > 0 and all(j > i for j in friends[i])
    all_nobles = set(range(1, n+1))
    while True:
        vulnerable = set(i for i in all_nobles if is_vulnerable(i))
        if not vulnerable:
            break
        all_nobles -= vulnerable
        for i in vulnerable:
            for j in friends[i]:
                friends[j].remove(i)
    answers = []
    for i in range(q):
        if queries[i][0] == 3:
            answers.append(len(all_nobles))
        else:
            u, v = queries[i][1:]
            if queries[i][0] == 1:
                friends[u].add(v)
                friends[v].add(u)
            else:
                friends[u].remove(v)
                friends[v].remove(u)
    return answers

n, m = map(int, input().split())
friends = defaultdict(set)
for i in range(m):
    u, v = map(int, input().split())
    friends[u].add(v)
    friends[v].add(u)
q = int(input())
queries = [list(map(int, input().split())) for i in range(q)]
answers = solve(n, m, q, friends, queries)
for a in answers:
    print(a)

