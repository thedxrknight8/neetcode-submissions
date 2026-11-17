class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            s_sorted = ''.join(sorted(s))

            m[s_sorted].append(s)
        
        ret = []
        for k in m:
            ret.append(m[k])
        
        return ret