class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if len(stack) == 0:
                    return False
                if stack.pop() != dict[i]:
                    return False

        return len(stack) == 0
                    
