class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for x in s:
            if x in d:
                stack.append(x)
            elif not stack or d[stack.pop()] != x:
                return False
        return not stack