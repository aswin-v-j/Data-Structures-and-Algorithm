class solution :
    def ispalindrome(self,s:str):
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1        
        return True
    
sol= solution()
str = "naman"
if sol.ispalindrome(str):
    print(f"{str} is a Palindrome")
else:
    print(f"{str} is not a Palindrome")