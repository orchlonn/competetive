from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = ans = 0
        increasing = deque()
        decreasing = deque()
        
        for right in range(len(nums)):
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()            
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()
            
            increasing.append(nums[right])
            decreasing.append(nums[right])
            
            while decreasing[0] - increasing[0] > limit:
                    if nums[left] == decreasing[0]:
                        decreasing.popleft()
                    if nums[left] == increasing[0]:
                        increasing.popleft()
                    left += 1
                
            ans = max(ans, right - left + 1)

        return ans
