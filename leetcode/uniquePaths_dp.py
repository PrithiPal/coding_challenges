class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        
        table = []
        for y in range(n) : 
            t=[]
            for x in range(m) : 
                t.append(0)
            table.append(t)
            
        
        table[0][0] = 1 
        
        for x in range(1,m) :
            table[0][x] = 1
        for y in range(1,n) : 
            table[y][0] = 1
            
            
        for x in range(1,m) : 
            
            for y in range(1,n) : 
                
                table[y][x] = table[y-1][x] + table[y][x-1]
                
        print(table)
        return table[n-1][m-1]
                
            
        
            
        
        
