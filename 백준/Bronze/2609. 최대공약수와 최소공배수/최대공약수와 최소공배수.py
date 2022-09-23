a, b = map(int, input().split())
gcd, lcm = 0, 0

lcm = a * b

if a >= b:
  gcd = a
  a = b
  b = gcd

while a % b != 0:
  gcd = a % b
  a = b
  b = gcd
gcd = b

lcm = lcm // gcd

print(gcd)
print(lcm)