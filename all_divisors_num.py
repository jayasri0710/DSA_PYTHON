class Solution:
    def alldivisors(self,n):
       ans=[]
       for i in range(1, n+1):
         if n%i==0:
            ans.append(i)
       return ans
obj=Solution()
n=int(input())
result=obj.alldivisors(n)
print(*result)
    
#print(*result)-->converting [1,5] to 1 5