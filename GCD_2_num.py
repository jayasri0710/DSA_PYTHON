class Solution:
    def gcd(self, a, b):
        # code here
        while b!= 0:
            a,b=b, a%b
        return a
obj=Solution()
a=int(input())
b=int(input())
result=obj.gcd(a,b)
print(result)