n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])