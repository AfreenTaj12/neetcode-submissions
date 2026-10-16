from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        # 1. CRITICAL: You must sort the array first!
        nums.sort()
      
        for i in range(0, n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            
            # 2. FIXED: Condition must check left < right
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # 3. FIXED: Wrap elements in a list []
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 4. FIXED: Skip duplicate elements for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward after finding a match
                    left += 1
                    right -= 1
                    
                elif current_sum > 0:
                    right -= 1
                else:
                    # 5. FIXED: Only increment left if the sum is too small
                    left += 1
                    
        return result
