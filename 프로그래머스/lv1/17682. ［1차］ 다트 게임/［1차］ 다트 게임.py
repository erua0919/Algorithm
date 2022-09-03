# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:28:24 2020

@author: wdp
"""


def solution(dartResult):
    answer = 0
    n = [str(i) for i in range(10)]
    a = ['S', 'D', 'T']
    li = []

    tmp1 = ''
    for i in range(len(dartResult)):
        if dartResult[i] in n:
            tmp1 += dartResult[i] 
        elif dartResult[i] in a:
            num = int(tmp1)
            if dartResult[i] == 'S':
                result = num**1     
            elif dartResult[i] == 'D':
                result = num**2   
            elif dartResult[i] == 'T':
                result = num**3   

            tmp1 = ''
            li.append(result)           
        elif dartResult[i] == '*':
            if len(li) >= 2:
                li[len(li)-2] = li[len(li)-2] * 2
                li[len(li)-1] = li[len(li)-1] * 2
            else:
                li[len(li)-1] = li[len(li)-1] * 2          

        elif dartResult[i] == '#':
            li[len(li)-1] = li[len(li)-1] * (-1)         

    answer = sum(li)
    return answer