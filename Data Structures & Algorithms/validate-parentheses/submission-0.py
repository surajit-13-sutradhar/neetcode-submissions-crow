class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # if the character is a closing bracket
                                                          # and top of stack is the correspondning 
                                                          # closing bracket   
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
            
        return True if not stack else False # return true if stack is empty