class Solution:
    def reverseexponentiation(self, n):
        # code here
        original=n
        rev=0
        while n > 0:
            digit=n%10
            rev=rev*10+digit
            n//=10
        pow=original**rev
        return pow