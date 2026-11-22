class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # so the same principle still applies
        # essentially, you would have to select one of everything and then drop it
        # the only thing is say you have [1, 2, 1, 2]. 

        # with the first one dfs, you get [1, 2]. but then you get the same with the second two
        # so you want to skip STARTING with the same one

        # we can sort 
        # and then skip ones that are the same through consecutive element comparison

        nums = sorted(nums)
        
        subsets = []
        subset = []

        def dfs(i):
            subsets.append(subset[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()
        
        dfs(0)

        return subsets
