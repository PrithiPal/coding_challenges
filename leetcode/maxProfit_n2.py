class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        
        if len(prices) >= 2 : 
            
            max_diff=prices[1]-prices[0] ## starter pack

            for i in range(len(prices)) : 

                for j in range(i+1,len(prices)) : 

                    if prices[j] - prices[i] > max_diff : 
                        max_diff = prices[j] - prices[i]

                        
            if max_diff < 0 :
                return 0 
            
            return max_diff
        
        return 0
        
        

