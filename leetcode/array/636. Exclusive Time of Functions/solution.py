class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # ["0:start:0","1:start:2","1:end:5","0:end:6"]
        # stack = [[0,6]]
        # res = [2-0 + (6-6+1),5-2+1]
        stack, res = [], [0] * n
        for log in logs:
            fid, ftype, timestamp = log.split(':')
            fid, timestamp = int(fid), int(timestamp)
            if ftype[0] == 's':
                if stack:
                    res[stack[-1][0]] += timestamp - stack[-1][1]
                stack.append([int(fid), int(timestamp)])
            else:
                tmpfid, tmpftimestamp = stack.pop()
                res[tmpfid] += timestamp - tmpftimestamp + 1
                if stack:
                    stack[-1][1] = timestamp + 1
                    
        return res
