class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        length = len(s)
        if not s:
            return True

        for char in t:
            if char == s[pointer]:
                pointer += 1
                if pointer == length:
                    return True
        return False

