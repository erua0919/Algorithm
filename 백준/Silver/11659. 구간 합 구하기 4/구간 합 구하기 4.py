N ,M = map (int, input().split())
numbers = list(map(int, input().split()))
#입력받은 i와 j 리스트로 정리
i_j_list =[]
for m in range(M):
    i_j = list(map(int,input().split()))
    i_j_list.append(i_j)
# prefix_sum 리스트 만들기    
prefix_sum = [0]
numbers_sum = 0
for number in numbers:
    numbers_sum += number
    prefix_sum.append(numbers_sum)
# prefix_sum을 사용해서 주어진 구간의 합 구하기    
for i_j in i_j_list:
    i , j = i_j[0], i_j[1]
    print(prefix_sum[j] - prefix_sum[i-1])