import sys
from math import inf


def bfs(s, t, antecessor, adj):
    V = range(len(adj))
    visitado = [False for _ in V]
    queue = []
    queue.append(s)
    visitado[s] = True

    while queue:
        u = queue.pop(0)
        for v, val in enumerate(adj[u]):
            if visitado[v] == False and val > 0:
                queue.append(v)
                visitado[v] = True
                antecessor[v] = u
                if v == t:
                    return True
    return False


def ford_fulkerson(source, target, _adj):
    print("ford_fulkerson")
    adj = _adj.copy()
    V = range(len(adj))
    antecessor = [-1 for _ in V]
    f = 0
    iter = 0
    while bfs(source, target, antecessor, adj):
        sys.stdout.write("\r%d" % iter)
        sys.stdout.flush()
        iter = iter+1
        fi = inf
        s = target
        while s != source:
            fi = min(fi, adj[antecessor[s]][s])
            s = antecessor[s]
        f += fi
        v = target
        while v != source:
            u = antecessor[v]
            adj[u][v] -= fi
            adj[v][u] += fi
            v = antecessor[v]
    sys.stdout.write("\n\n")
    return f
