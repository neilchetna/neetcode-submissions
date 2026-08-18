class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = [0] * 26

        if len(s) != len(t): 
            return False

        for i in range(len(s)):
            x = ord(s[i]) - 97
            y = ord(t[i]) - 97

            hm[x] += 1
            hm[y] -= 1

        return max(hm) == 0 and min(hm) == 0