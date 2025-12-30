# first create a class "marriage"
# then variables => dresscolour, jewels, garlands
#  / function => def bride():
# callling class=>   bride=marriage()
# calling variables => 
# calling funct => hp.display() => display - name of funct ,hp- name of object



class Solution:
    def getLastDigit(self, a, b):
        return(pow(int(a), int(b), 10))
a=input("print a:")
b=input("print b:")
sol=Solution()
print(sol.getLastDigit(a, b))