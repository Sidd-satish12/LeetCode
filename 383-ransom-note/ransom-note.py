class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for letter in magazine:
            if letter not in map:
                map[letter] = 1
            else:
                map[letter] += 1
        
        for letter in ransomNote:
            try:
                if map[letter]:
                    map[letter] -= 1
                else:
                    return False
            except KeyError:
                return False
        return True