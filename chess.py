

import time     
    
def foo(grid,x,n) : 
    
    if x==n: ## end of search from here.
        return True 

    ## y iteration 
    
    for i in range(n)  : 
        if i==0 : 
            if grid[x-1][i] or grid[x-1][i+1] : 
                continue
        elif i==n-1 : 
            if grid[x-1][i-1] or grid[x-1][i] : 
                continue
        else:
            if grid[x-1][i-1] or grid[x-1][i] or grid[x-1][i+1] : 
                continue
            
        grid[x][i]=1
        
        printGrid(grid)
        
        time.sleep(1)
        
        if foo(grid,x+1,n) : 
            return True 
            

def printGrid(grid) : 
    
    for row in grid : 
        print(row)
        

def solve(n) : 
    
    grid=[]

    for i in range(n) : 
        grid.append([0 for i in range(n)])
        
    grid[0][0]=1
    
    #printGrid(grid)
    foo(grid,1,n)
    printGrid(grid)
    
            
solve(10)
        
