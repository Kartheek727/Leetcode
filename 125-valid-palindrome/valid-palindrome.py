import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= re.sub(r'[^a-zA-Z0-9\s]', '', s)
        s=s.replace(" ","")
        crt=s
        rev= crt[::-1]
        if(crt==rev):
            return True
        else:
            return False