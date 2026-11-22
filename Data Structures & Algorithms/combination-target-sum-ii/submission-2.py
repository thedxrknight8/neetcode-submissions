class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = []

        candidates = sorted(candidates)

        def dfs(i, s):
            if s > target:
                return 
            
            if s == target:
                ret.append(temp[:])
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                temp.append(candidates[j])
                dfs(j + 1, candidates[j] + s)
                temp.pop()
        dfs(0, 0)
        return ret
