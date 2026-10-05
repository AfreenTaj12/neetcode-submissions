class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count occurrences of each number
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
        # Step 2: Sort the unique keys based on their value counts
        # reverse=True places the most popular numbers at the front
        sorted_numbers = sorted(count_map.keys(), key=count_map.get, reverse=True)
        
        # Step 3: Grab the top 'k' elements
        return sorted_numbers[:k]



        