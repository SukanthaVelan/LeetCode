class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)):
            if s[i] in '({[':
                l.append(s[i])
            else:
                if l:
                    x = l.pop()
                    if (x == "(" and s[i] ==")") or (x == "{" and s[i] =="}") or (x == "[" and s[i] =="]"):
                        print(x,s[i],"*")
                    else:
                        l.append(x)
                        break
                else:
                    l.append(s[i])
        if l == []:
            return 1
        else:
            return 0
    
                
        