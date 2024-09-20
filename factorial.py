class solution:
    def factorial(self,num):
        if num == 0 or num == 1:
            return 1
        
        else :
            return num * self.factorial(num-1) 

n = 5
sol = solution()
print(sol.factorial(n))
