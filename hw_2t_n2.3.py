
s = input()
m = []
i = 0
while i < len(s):
    m.append((s[i:] + s[:i],i))
    i +=1
m.sort()
b = 0
st =''
for pos, (sl, idx) in enumerate(m, 1):
    if idx ==0 and b == 0:
        b = pos
    st += sl[-1]
print(b)
print(st)
