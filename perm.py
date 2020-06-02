## computing permutation

import copy 

def perm(subset,arr,indlist) :
    
    ## full permutation has been made here
    
    if len(subset)==len(arr) : 
        print(subset)
        return 1

    c = 0 
    for i in range(len(arr)) : 
        
        if i not in indlist : 
            
            indlist.append(i)
            subset.append(arr[i])
            
            c = c + perm(subset,arr,indlist) 
                
            subset.pop()
            indlist.pop()
            
    return c 
    

            
    
def perm_caller(arr) : 
    c=0
    for i in range(len(arr)) : 
        c = c + perm([arr[i]],arr,[i])
        
    return c 
    
    
x=perm_caller(list(range(100)))
print(x)
