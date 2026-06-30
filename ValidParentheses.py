class Solution:
    def isValid(self, s: str) -> bool:
        pstack = []
        for char in s:
            if(char == '(' or char == '[' or char == '{'):
                pstack.append(char)
            else:
                if(len(pstack) == 0):
                    return False
                if(char ==')'):
                    if(pstack[-1] == '('):
                        pstack.pop()
                    else:
                       return False
                if(char == '}'):
                    if(pstack[-1] == '{'):
                       pstack.pop()
                    else:
                       return False
                if(char == ']'):
                    if(pstack[-1] == '['):
                        pstack.pop()
                    else:
                       return False
        if(len(pstack) == 0):
            return True
        return False

