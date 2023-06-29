class Solution:
    def compress(self, chars: List[str]) -> int:

        new_chars = []
        idx = 0

        while idx < len(chars):
            cc = chars[idx]

            cnt = 0
            while idx < len(chars) and chars[idx] == cc:
                cnt += 1
                idx += 1

            new_chars.append(cc)
            if cnt > 1:
                for x in str(cnt):
                    new_chars.append(x)
                
        chars[:]=new_chars
        return