class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in hash:
                hash[nums[i]] = i
            else:
                return [hash[diff], i]