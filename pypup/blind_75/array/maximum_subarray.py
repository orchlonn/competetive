def maximum_subarray(nums):
    maxSub = nums[0]
    curSum = 0
    
    for i in nums:
        if(curSum < 0):
            curSum = 0
        curSum += i
        maxSub = max(maxSub, curSum)
        
    return maxSub
        
