class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) >= 2 : 
        

            c = prices[1]-prices[0]

            for i in range(len(prices)) : 
                val = prices[i]
                max_val = max(prices[i:])

                if max_val-val > c : 
                    c = max_val-val

            return c 
        
        else:
            return 0 





