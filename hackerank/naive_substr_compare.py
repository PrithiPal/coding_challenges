

## ABBA LEN = 2 ; ab, bb ,ba 
## 0,1,2

def countDict(arr) : 
    d = {}
    for ch in arr : 
        if ch in d : 
            d[ch]=d[ch]+1
        else:
            d[ch]=1
            
    return d 

def lenSubstr(n,arr) : 
    
    count = 0 
    for i in range(0,len(arr)-n+1) :
        
        s1 = arr[i:i+n]
        
        for j in range(i+1,len(arr)-n+1) : 
            
            s2 = arr[j:j+n]
            if countDict(s1) == countDict(s2) : 
                count = count + 1 
                print("{} {}".format(s1,s2))
            
            #print("{} {}".format(s1,s2))
            
    return count

def countSubstrs(arr) : 
    
    count = 0 
    
    for i in range(len(arr)) :  ## 0 , 1  .. n-1
        count = count + lenSubstr(i+1,arr)
    
    return count 
        
        
print(countSubstrs("ABBA"))
        
