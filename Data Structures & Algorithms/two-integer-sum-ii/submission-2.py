class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L, R = 0, len(numbers) - 1

        for i in range(len(numbers)):
            sum = numbers[L] + numbers[R]
            if sum == target:
                return [L + 1, R + 1]
            elif sum < target:
                L += 1
            else:
                R -= 1