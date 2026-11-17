class Solution:
    def encode(self, strs: List[str]) -> str:
        enc = []

        for s in strs:
            enc.append(f"{len(s)}#{s}")
        
        return "".join(enc)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length_to_read = []
            while s[i] != "#":
                length_to_read.append(s[i])
                i += 1
            
            length_to_read = int("".join(length_to_read))
            
            i += 1
            j = i
            
            temp = []
            while j < length_to_read + i:
                temp.append(s[j])
                j += 1

            res.append("".join(temp))
            i = j
        return res
