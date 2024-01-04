"""
Problem:
https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75

Solution:
https://leetcode.com/problems/dota2-senate/solutions/3483399/simple-diagram-explanation/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = []
        dire = []
        n = len(senate)

        for idx, senator in enumerate(senate):
            if senator == "R":
                rad.append(idx)
            else:
                dire.append(idx)

        while rad and dire:
            rad_idx = rad.pop(0)
            dire_idx = dire.pop(0)

            if rad_idx < dire_idx:
                rad.append(n)
            else:
                dire.append(n)

            n += 1

        if rad:
            return "Radiant"

        return "Dire"


if __name__ == "__main__":
    solution = Solution()
    print(solution.predictPartyVictory(senate="RD"))
    print(solution.predictPartyVictory(senate="RDD"))
    print(solution.predictPartyVictory(senate="DDRRRR"))
    print(solution.predictPartyVictory(senate="DDRRR"))
    print(solution.predictPartyVictory(senate="RDRDRDD"))
    print(solution.predictPartyVictory(senate="DRRDRDRDRDDRDRDR"))
