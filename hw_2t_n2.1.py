def f(s):
    n = len(s)
    for i in range(1, n+1):
        if n % i == 0:
            if s[:i] * (n//i) == s:
                return i
    return n

t = int(input())
res = []
for q in range(t):
    s = input()
    res.append(str(f(s)))

print('\n'.join(res))
