class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
    
        return self.build(s) == self.build(t)
    
    def build(self, s):
        stack = []
        for c in s:
            if c != "#":
                stack.append(c)
            elif stack:
                stack.pop()
                
        return ''.join(stack)