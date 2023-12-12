class Solution:
    def simplifyPath(self, path: str) -> str:
        a= path.split("/")
        answer=[]
        for x in a:
            if x in ("",".") :
                continue
            elif x == "..":
                if answer:
                    answer.pop()
                else:
                    continue
            else:
                answer.append(x)
        return "/" + "/".join(answer)