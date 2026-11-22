class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        temp = []

        def dfs(i):
            ret.append(temp[:])

            for j in range(i, len(nums)):
                temp.append(nums[j])
                dfs(j + 1)
                temp.pop()
        dfs(0)
        return ret