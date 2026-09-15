import sys
sys.setrecursionlimit(300000)

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
size = [1] * (n + 1)
heavy = [-1] * (n + 1)

# Find parent, depth and subtree sizes
stack = [1]
order = []

while stack:
    u = stack.pop()
    order.append(u)
    for v in graph[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        depth[v] = depth[u] + 1
        stack.append(v)

for u in reversed(order):
    max_size = 0
    for v in graph[u]:
        if parent[v] == u:
            size[u] += size[v]
            if size[v] > max_size:
                max_size = size[v]
                heavy[u] = v

# Heavy-Light Decomposition
head = [0] * (n + 1)
pos = [0] * (n + 1)
cur = 0

stack = [(1, 1)]

while stack:
    u, h = stack.pop()

    while u != -1:
        head[u] = h
        pos[u] = cur
        cur += 1

        for v in graph[u]:
            if parent[v] == u and v != heavy[u]:
                stack.append((v, v))

        u = heavy[u]

# Segment tree
size_tree = 1
while size_tree < n:
    size_tree <<= 1

tree = [0] * (2 * size_tree)

# Every edge is initially active.
# Root has no edge, so its value is 0.
for u in range(2, n + 1):
    tree[size_tree + pos[u]] = 1

for i in range(size_tree - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]

def update(p):
    i = size_tree + p
    tree[i] ^= 1

    i >>= 1
    while i:
        tree[i] = tree[2 * i] + tree[2 * i + 1]
        i >>= 1

def query(l, r):
    if l > r:
        return 0

    l += size_tree
    r += size_tree
    ans = 0

    while l <= r:
        if l & 1:
            ans += tree[l]
            l += 1
        if not (r & 1):
            ans += tree[r]
            r -= 1
        l >>= 1
        r >>= 1

    return ans

def path_query(u, v):
    ans = 0

    while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u

        ans += query(pos[head[u]], pos[u])
        u = parent[head[u]]

    if depth[u] > depth[v]:
        u, v = v, u

    # Exclude u because u represents the edge from parent[u] to u.
    # When u is the LCA, that edge is not part of the path.
    ans += query(pos[u] + 1, pos[v])

    return ans

q = int(input())

out = []

for _ in range(q):
    event = list(map(int, input().split()))

    if event[0] == 1:
        v = event[1]
        update(pos[v])
    else:
        u, v = event[1], event[2]
        out.append(str(path_query(u, v)))

sys.stdout.write("\n".join(out))