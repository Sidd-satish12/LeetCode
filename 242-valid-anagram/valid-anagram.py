class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in map:
                map[letter] += 1
            else:
                map[letter] = 1
        
        for letter in t:
            if letter not in map or not map[letter]:
                return False
            map[letter] -= 1
        return True