def maxStrawberries(A, num):
    n = len(A)
    F = [[False] * (num + 1) for _ in range(n + 1)]
    G = [[False] * (num + 1) for _ in range(n + 1)]
    F[0][0], G[0][0] = True, True
    for i, x in enumerate(A):
        F[i + 1] = [g | (y >= x and G[i][y - x]) for y, g in enumerate(G[i])]
        G[i + 1] = [f | g for f, g in zip(F[i], G[i])]
    return num - min(F[-1][::-1].index(True), G[-1][::-1].index(True))