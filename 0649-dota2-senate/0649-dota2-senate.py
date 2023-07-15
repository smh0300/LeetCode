class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        rq= deque()
        dq= deque()
        idx = len(senate)

        for x,y in enumerate(senate):
            rq.append(x) if y=="R" else dq.append(x)

        while rq and dq:
            if rq[0] < dq[0]:
                dq.popleft()
                rq.append(idx)
                idx += 1
                rq.popleft()
            else:
                rq.popleft()
                dq.append(idx)
                idx += 1
                dq.popleft()

        if rq:
            return "Radiant"
        else:
            return "Dire"
