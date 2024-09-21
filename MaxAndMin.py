class solution :
    def findsum(self,A,N) :

        if N == 1 :
            return A[0]
        
        if A[0] > A[1] :
            maxi = A[0]
            mini = A[1]
        else :
            maxi = A[1]
            mini = A[0]      

        for i in range(2,N) :
            if A[i] > maxi :
                maxi = A[i]
            elif A[i] < mini :
                mini = A[i]

        print( mini + maxi) 

l = [2,-1,7,10]
n = 4
arr1 = solution()
arr1.findsum(l,n)
