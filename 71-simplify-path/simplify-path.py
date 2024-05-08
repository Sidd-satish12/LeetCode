class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s_path = ""
        directory_list = path.split('/')

        for directory in directory_list:
            if directory == '.' or directory == '':
                continue
            if directory == '..':
                if stack:
                    stack.pop()
            else:
                 stack.append(directory)
        
        s_path = '/' + '/'.join(stack)
        return s_path
