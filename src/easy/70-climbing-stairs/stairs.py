# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        combos = 0
        max_pairs = n // 2

        for pairs in range(max_pairs + 1):
            # trying combinations with i pairs of two
            combos += self.combinations(pairs, n)

        return combos

    def combinations(self, pairs: int, positions: int) -> int:
        # how many combinations to fit pairs pairs into positions?
        if (pairs <= 0):
            return 1

        combos = 0

        for i in range(positions - 1):
            # start with pair and check all other combinations
            combos += self.combinations(pairs-1, positions - (i+2))

        return combos

# TODO exceeds timelimit since values get calculated recursively miltiple times
#  => memoization?
