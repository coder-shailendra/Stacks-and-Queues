class Solution(object):
    def isValid(self, s):
        n = len(s)
        if n % 2 == 1:
            return False
        st = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            else:
                if len(st) == 0:
                    return False
                top = st.pop()
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False
        return len(st) == 0
obj = Solution()
print(obj.isValid("()"))       
print(obj.isValid("()[]{}")) 
print(obj.isValid("(]"))        
     