def solution(x):
    orgin = x
    sum = 0

    x = list(str(x))

    for n in x:
        sum += int(n)

    return orgin % sum == 0