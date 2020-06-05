class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(t) < len(s) : 
            return False
        elif len(t)==len(s) : 
            
            return t==s
        
        elif len(s)==0 : 
            return True 
        
        sec_list = [x for x in s]
        
        for i in range(len(s)) : 
            
            if self.foo(t,i,[t[i]],sec_list) : 
                print("yes")
                return True
            
        return False
            
            
    
    def foo(self,arr,ind,subarray,target) :
        #print(subarray)
        
        if target==subarray:
            return True 
    
        for i in range(ind+1,len(arr)) : 
            subarray.append(arr[i])
            
            if self.foo(arr,i,subarray,target) : 
                return True 
            
            subarray.pop()
            
        return False
            
        
        
        
