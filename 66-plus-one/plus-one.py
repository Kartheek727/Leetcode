class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=0
        for i in range(len(digits)):
            res=res*10 + digits[i]
        res=res+1
        ans=list(map(int,str(res)))
        return ans
        