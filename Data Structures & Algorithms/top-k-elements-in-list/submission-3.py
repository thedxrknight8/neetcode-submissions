class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # make a key of every frequency possible
        # then create a Counter for elements in nums
        # then look from the back of the array 

        counter = Counter(nums)
        freqs = []
        for _ in range(len(nums) + 1):
            freqs.append([])

        for num in counter:
            freqs[counter[num]].append(num)
        
        ret = []
        for i in range(len(freqs) - 1, -1, -1):
            for num in freqs[i]:
                ret.append(num)
            
            if len(ret) == k:
                break
        
        return ret
                



        
            



