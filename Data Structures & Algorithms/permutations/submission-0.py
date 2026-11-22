class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        used = set()
        temp = []

        def dfs():
            if len(temp) == len(nums):
                ret.append(temp[:])
                return
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    temp.append(num)
                    dfs()
                    used.remove(num)
                    temp.remove(num)
        dfs()
        return ret

