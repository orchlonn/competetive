from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            
            # checking the sliding window reaches the k
            if queue[0] + k == i:
                queue.popleft()
            
            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])
                
        return ans
