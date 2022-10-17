def Addition(f, g, mod):
    degf = len(f)
    degg = len(g)
    if degf>degg:
        ax = f
        f = g
        g = ax
        ax = degf
        degf = degg
        degg = ax
    for i in range(0, degf):
        g[i]=(f[i]+g[i])%mod
    return g

def Substraction(f, g, mod):
    degf = len(f)
    degg = len(g)
    if degf < degg:
        for i in range(0, degf):
            g[i] = (f[i] - g[i]) % mod
        for i in range(degf, degg):
            g[i] = (0 - g[i]) % mod
        return g
    else:
        for i in range(0, degg):
            f[i] = (f[i] - g[i]) % mod
        return f

print(Substraction([2, 1], [1, 0, 2], 3))




