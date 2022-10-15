import math
import sys
while(True):
    n = sys.stdin.readline().strip()
    if(n=='0'):
        break
    else:
        length=len(n)
        sum=0
        for i in range(1,length+1):
            n=int(n)
            sum+=int(n%10)*(math.factorial(i))
            n/=10
        print(sum)