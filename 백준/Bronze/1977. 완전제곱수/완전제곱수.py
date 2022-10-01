n=int(input())
m=int(input())
t=[i**2 for i in range(101) if n<=i**2 <=m]
print(f'{sum(t)}\n{t[0]}'if t else -1)