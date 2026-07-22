class Solution(object):
    def backspaceCompare(self, s, t):
        def build(string):
            stack=[]
            for ch in string:
                if ch!="#":
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack
        return build(s)==build(t)                
        