class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        if len(cost)==1 : 
            return cost[0]
        
        elif len(cost)==2 : 
            return max(cost)
        
        else:
            first = self.minCost(cost,0,cost[0])
            second = self.minCost(cost,1,cost[1])

            return min(first,second)
        
        
    def minCost(self,arr,ind,target) : 
        
        if ind>=len(arr)-1 : 
            return target 
       
        if ind+1 <= len(arr)-1 : 
            first = self.minCost(arr,ind+1,target+arr[ind+1])
        else:
            first = target 
            
        if ind+2 <= len(arr)-1 :  
            second = self.minCost(arr,ind+2,target+arr[ind+2])
        else:
            second = target

        return min(first,second)

        
            
        
