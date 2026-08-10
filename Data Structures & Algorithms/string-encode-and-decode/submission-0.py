class Solution:

    def encode(self, strs: List[str]) -> str:
        # have a # to indicate the stop of the length
        # before that have the number of characters that we want to iterate
        # then iterate the amount of characters after the hash

        res = []

        for s in strs: 
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        print(s)
        while i < len(s):
            length = []
            while s[i] != "#":
                length.append(s[i])
                i += 1
            length = int("".join(length))
            
            temp = []
            j = i + 1
            while j < i + length + 1:
                temp.append(s[j])
                j += 1
            res.append("".join(temp))
            temp = []
            i = j
        
        return res

            
            