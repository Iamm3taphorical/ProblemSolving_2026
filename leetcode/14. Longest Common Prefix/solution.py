class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        
        idx = 0
        while idx < len(first) and idx < len(last):
            if first[idx] == last[idx]:
                idx += 1
            else:
                break
        
        return first[:idx]
