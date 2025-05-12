from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.player_score = collections.defaultdict(int)
        self.score_num = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        pre_score = self.player_score[playerId]
        if -pre_score in self.score_num:
            if self.score_num[-pre_score] == 1:
                del self.score_num[-pre_score]
            else:
                self.score_num[-pre_score] -= 1
        self.player_score[playerId] += score
        if -self.player_score[playerId] not in self.score_num:
            self.score_num[-self.player_score[playerId]] = 1
        else:
            self.score_num[-self.player_score[playerId]] += 1

    def top(self, K: int) -> int:
        res = 0
        count = 0
        for key, val in self.score_num.items():
            for i in range(val):
                res += -key
                count += 1
                if count == K:
                    break
            if count == K:
                break
        return res

    def reset(self, playerId: int) -> None:
        score = self.player_score[playerId]
        if self.score_num[-score] == 1:
            del self.score_num[-score]
        else:
            self.score_num[-score] -= 1
        del self.player_score[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
