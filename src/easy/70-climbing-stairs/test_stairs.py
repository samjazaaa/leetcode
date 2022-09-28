from stairs import Solution


class TestStairs:
    def test_one(self):
        # x
        assert Solution().climbStairs(1) == 1

    def test_two(self):
        # x x
        # xx
        assert Solution().climbStairs(2) == 2

    def test_three(self):
        # x x x
        # xx x
        # x xx
        assert Solution().climbStairs(3) == 3

    def test_four(self):
        # x x x x
        # xx x x
        # x xx x
        # x x xx
        # xx xx
        assert Solution().climbStairs(4) == 5

    def test_five(self):
        # x x x x x
        # xx x x x
        # x xx x x
        # x x xx x
        # x x x xx
        # xx xx x
        # xx x xx
        # x xx xx
        assert Solution().climbStairs(5) == 8

    def test_six(self):
        # x x x x x x
        # xx x x x x
        # x xx x x x
        # x x xx x x
        # x x x xx x
        # x x x x xx
        # xx xx x x
        # xx x xx x
        # xx x x xx
        # x xx xx x
        # x xx x xx
        # x x xx xx
        # xx xx xx
        assert Solution().climbStairs(6) == 13
