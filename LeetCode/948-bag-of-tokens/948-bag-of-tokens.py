class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        res = score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if tokens[l] <= P:
                P -= tokens[l]
                score += 1
                res = max(res, score)
                l += 1
            else:
                if score:
                    score -= 1
                    P += tokens[r]
                    r -= 1
                else:
                    break
        return res
        