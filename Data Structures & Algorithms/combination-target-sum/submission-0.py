class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        ret = []

        def dfs(s, i):
            if s > target:
                return
            elif s == target:
                ret.append(temp[:])
                return
            
            for j in range(i, len(nums)):
                temp.append(nums[j])
                dfs(nums[j] + s, j)
                temp.pop()
        dfs(0, 0)
        return ret