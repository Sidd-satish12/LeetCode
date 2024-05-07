class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        word_list = s.split(' ')
        index = 0
        print(word_list)
        while index < len(pattern) and index < len(word_list):
            print(index)
            if pattern[index] not in map and word_list[index] in map.values():
                return False
            map[pattern[index]] = word_list[index]
            index += 1
        index = 0
        for word in word_list:
            if index >= len(pattern):
                return False
            if map[pattern[index]] != word:
                return False
            
            index += 1
        
        if index < len(pattern):
            return False
        
        return True