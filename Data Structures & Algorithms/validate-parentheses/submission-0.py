class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c not in mapping:
                st.append(c)
            else:
                if not st or mapping[c] != st[-1]:
                    return False
                else:
                    st.pop()
        
        return not st