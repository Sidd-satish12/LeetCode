class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}

        for index, char in enumerate(s):
            if char not in map:
                if t[index] in map.values():
                    print(t[index],char)
                    return False
                map[char] = t[index]
            elif map[char] != t[index]:
                return False
        return True