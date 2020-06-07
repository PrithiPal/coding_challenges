class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        num_arr = [int(x) for x in str(num)]

        shortest_str = self.removeKdigitsRecurse(num_arr,0,k)
        return "".join([str(y) for y in shortest_str])
    
    def removeKdigitsRecurse(self,arr,cut,k) : 
        if cut==k or len(arr)==1: 
            #print(arr)
            return arr
        
        local_minima=int("".join([str(y) for y in arr]))
        local_best_subarr=arr[:0] + arr[1:]
        
        for i in range(len(arr)) : 
            subarr = arr[:i] + arr[i+1:]
            
            
            s = self.removeKdigitsRecurse(subarr,cut+1,k)
            s_number = int("".join([str(y) for y in s]))
            
            
            if s_number < local_minima : 
                
                local_minima = s_number
                #print(local_minima)
                local_best_subarr = s
            
        #print(local_best_subarr)    
        return local_best_subarr
    
    
    
