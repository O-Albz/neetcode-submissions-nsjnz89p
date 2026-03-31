class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        HashTable = {}

        for num in nums:
            if num not in HashTable:
                HashTable[num] = HashTable.get(num, 0) + 1
            else:
                HashTable[num] += 1

        max_keys = sorted(HashTable, key = HashTable.get, reverse = True)

        return max_keys[:k]