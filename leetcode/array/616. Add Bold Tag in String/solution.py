class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # aaabbb  ["aa","b"]
        # iterate every word and find the word in the substring of string
        intervals = []
        for word in words:
            wordlen = len(word)
            for i in range(len(s) - wordlen + 1):
                tmps = s[i:i+wordlen]
                if word == tmps:
                    # added these to the intervals
                    intervals.append([i, i+wordlen-1])
        # if the interval is empty, return s
        if not intervals:
            return s
        # sort the intervals
        intervals.sort()
        merged_intervals = []
        # merge the intervals
        for start, end in intervals:
            if not merged_intervals:
                merged_intervals.append([start, end])
            else:
                last_start, last_end = merged_intervals[-1][0], merged_intervals[-1][1]
                if start <= last_end + 1:
                    new_end = max(end, last_end)
                    merged_intervals[-1][1] = new_end
                else:
                    merged_intervals.append([start, end])
        # print(merged_intervals)
        # add the bold tag to the merged intervals
        res = []
        prev_ind = 0
        for start, end in merged_intervals:
            if prev_ind < start:
                res.append(s[prev_ind:start])
            res.append('<b>')
            res.append(s[start:end+1])
            res.append('</b>')
            prev_ind = end + 1
        if prev_ind < len(s):
            res.append(s[prev_ind:])
        return ''.join(res)
