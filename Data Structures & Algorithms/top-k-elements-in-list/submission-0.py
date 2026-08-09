class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = [[] for _ in range(len(nums) + 1)]
        count = defaultdict(int)
        
        for i in nums:
            count[i] += 1
        for l in count:
            m[count[l]].append(l)
        
        res = []
        for i in range(len(m) - 1, 0, -1):
            for j in m[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        return []
