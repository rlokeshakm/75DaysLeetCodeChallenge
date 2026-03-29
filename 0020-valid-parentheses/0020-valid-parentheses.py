class Solution:
    def isValid(self, s: str) -> bool:
        maps={")":"(", "]":"[" ,"}":"{"}
        stack=[]

        for i in s:
            if i in maps.values():
                stack.append(i)
            elif i in maps:
                if not stack or maps[i]!=stack.pop():
                    return False
        return not stack

        