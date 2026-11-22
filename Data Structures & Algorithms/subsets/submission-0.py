class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def dfs(i, temp):
            # iterate from point i onwards and select one of everything for a dfs call 
            ret.append(temp[:])
            # you append that thing 
            # and then you remove it after the dfs is done;
            # this means that you explore all paths from that point
            # and then remove it when you are done
            # and then move on to the next selection
            
            for j in range(i, len(nums)):
                temp.append(nums[j])
                dfs(j + 1, temp)
                temp.pop()

        dfs(0, [])
        return ret