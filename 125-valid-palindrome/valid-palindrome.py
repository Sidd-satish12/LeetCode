class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_index = len(s) - 1
        index = 0
        while index <= reverse_index:
            if s[index].isalnum():
                while not s[reverse_index].isalnum():
                    reverse_index -= 1
                
                if s[index].lower() != s[reverse_index].lower():
                    print(s[index], index)
                    print(s[reverse_index], reverse_index)
                    return False
                reverse_index -= 1
            index += 1
        return True
        