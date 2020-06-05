class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memoize_hash={}
       
        
        if len(cost)==1 : 
            return cost[0]
        
        elif len(cost)==2 : 
            return max(cost)
        
        else:
            first = self.minCost(cost,0,cost[0],memoize_hash)
            second = self.minCost(cost,1,cost[1],memoize_hash)

            print(memoize_hash)
            return min(first,second)
        
        
    def minCost(self,arr,ind,target,table) : 
        
        if ind>=len(arr)-1 : 
            return target 
       
        if ind+1 <= len(arr)-1 : 
            
            first_key = "({},{})".format(ind+1,target+arr[ind+1],table)
            
            if first_key in table : 
                first = table[first_key]
            else:
                first = self.minCost(arr,ind+1,target+arr[ind+1],table)
                table['({},{})'.format(ind+1,target+arr[ind+1])] = first
        else:
                
            
            first = target 
            
        
            
        if ind+2 <= len(arr)-1 :  
            
            second_key = "({},{})".format(ind+2,target+arr[ind+2])
            
            if second_key in table : 
                second = table[second_key]
            else:
                second = self.minCost(arr,ind+2,target+arr[ind+2],table)
                table['({},{})'.format(ind+2,target+arr[ind+2])] = second
        else:
            second = target

               
        
        return min(first,second)

        
            
        
