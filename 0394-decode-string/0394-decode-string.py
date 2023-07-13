class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        answer=""
        tmps = ""
        nums = ""
        for x in s:
            if x == "]":
                while stack and stack[-1] != "[":
                    tmp = stack.pop()
                    tmps = tmp + tmps
                stack.pop()
                tmps = tmps + answer
                while stack and str(stack[-1]).isdecimal():
                    nums = str(stack.pop()) + nums

                for y in range(int(nums)):
                    answer += tmps

                stack.append(answer)

                answer, nums, tmps = "", "", ""
            else:
                stack.append(x)

        for x in stack:
            answer += x
        return answer