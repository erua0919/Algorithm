L = int(input())
string = input()
result = 0

for i in range(L):
    result += (ord(string[i])-96) * (31 ** i)
print(result % 1234567891)