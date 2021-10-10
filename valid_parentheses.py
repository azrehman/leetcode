class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # map with open braces as keys and closing as values
        open_close_map = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            # push if opening
            if c in open_close_map:
                stack.append(c)
            # for closing, return false if stack is empty or top element does not match
            else:
                if not stack or c != open_close_map[stack.pop()]:
                    return False
        # return valid if stack is empty
        return not stack

