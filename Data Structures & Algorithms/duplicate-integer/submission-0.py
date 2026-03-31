class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       seen_numbers = []
       for i in range(len(nums)):
            if nums[i] in seen_numbers:
                return True
            else:
                seen_numbers.append(nums[i])

       return False