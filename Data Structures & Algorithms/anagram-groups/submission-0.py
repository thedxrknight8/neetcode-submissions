class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            m["".join(sorted(s))].append(s)
        
        l = []
        for key in m:
            l.append(m[key])
        
        return l