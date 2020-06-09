import math


## complexity is O(log10(N))
def numberSum(n) : 
    
    
    numSum = 0 
    
    while n>=1 : 
        
        numSum = numSum + ( n % 10 )
        n = math.floor(n/10)
        
    return numSum
    
    

def equalDigitSumMaxPair(arr) : 
    hash_map = {}
    no_pair = True
    ## O(n)
    
    for i in range(len(arr)) : 
        if numberSum(arr[i]) in hash_map : 
            no_pair = False ## atleast one pair exists.
            hash_map[numberSum(arr[i])].append(arr[i])
        else:
            
            hash_map[numberSum(arr[i])] = [arr[i]]
            
    print(hash_map)
    
    if no_pair : 
        return -1
    
    for k in hash_map : 
        hash_map[k] = sorted(hash_map[k],reverse=True)
    print(hash_map)
    
    maxPairSum=min(arr[:2])
    for k in hash_map : 
        if sum(hash_map[k][:2]) > maxPairSum : 
            maxPairSum=sum(hash_map[k][:2])
    
    
    return maxPairSum
            
            
print(equalDigitSumMaxPair([51,32,43]))
#print(numberSum(51))
    
        
