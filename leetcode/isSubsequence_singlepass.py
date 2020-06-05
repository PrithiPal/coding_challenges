class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t) : 
            return False
        elif len(s)==0 : 
            return True
        elif len(s)==len(t):
            return s==t
        else:
            c = 0  
            substr = [x for x in s]
            cmpstr = [x for x in t]



            for i in range(len(cmpstr)) : 

                if cmpstr[i]==substr[c] : 
                    c=c+1
                    if c==len(substr):
                        return True 

            return False
