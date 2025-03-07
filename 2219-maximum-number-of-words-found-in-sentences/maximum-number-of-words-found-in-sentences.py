class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in range(len(sentences)):
            s=sentences[i]
            count=1
            for j in range(len(s)):
                ch = s[j]
                if(ch==" "):
                    count+=1
            ans=max(ans,count)
        return ans
        
        

            
            

   
        

        