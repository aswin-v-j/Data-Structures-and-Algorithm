class solution:
    def stringreverse(self,arr):
        left ,right = 0,len(a)-1
    
        while left<right:
            temp = a[left]
            a[left] = a[right]
            a[right]  = temp 
            left += 1
            right -= 1
        print (a)

sol = solution()
a = [1,6,3,5,8]
sol.stringreverse(a)