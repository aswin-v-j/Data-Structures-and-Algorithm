class solution:
    def removeduplicates(self,s):
        if not s :
            return 0
        
        unique = 0

        for i in range(1,len(s)):
            if s[i] != s[unique]:
                unique +=1 
                s[unique] = s[i]

        return unique + 1    
        
sol  = solution()
arr = [1,1,1,2,3,5]
a = sol.removeduplicates(arr)
print(a)
