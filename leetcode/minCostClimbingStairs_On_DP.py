class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        table = []
        table.append(cost[0])
        table.append(cost[1])
        
        for i in range(2,len(cost)) : 
            table.append(cost[i] + min(table[i-1],table[i-2]))
            
        return min(table[len(cost)-1],table[len(cost)-2])

        
            
        
