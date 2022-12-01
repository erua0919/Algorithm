class Solution:
    def halvesAreAlike(self, s):
        check=('aeiouAEIOU')
        f_s=0
        b_s=0
        for i in range(len(s)//2):
            if s[i] in check:
                f_s+=1
            if s[-i-1] in check:
                b_s+=1
               
        return f_s==b_s