# https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        prev_colided = False
        collisions = 0
        stacked = 0
        for i in range(1, len(directions)):
            if (directions[i] == 'L'):
                if (directions[i-1] == 'R'):
                    collisions += 2
                    collisions += max([0, (stacked - 1)])
                    stacked = 0
                    prev_colided = True
                elif (prev_colided or directions[i-1] == 'S'):
                    collisions += 1
                    prev_colided = True
                else:
                    prev_colided = False
            elif (directions[i] == 'R'):
                prev_colided = False
                stacked += 1
                if (i == 1 and directions[0] == 'R'):
                    stacked += 1
            elif (directions[i] == 'S'):
                if (directions[i-1] == 'R'):
                    collisions += 1
                    collisions += max([0, (stacked - 1)])
                    stacked = 0
                    prev_colided = True
                else:
                    prev_colided = False
            else:
                return -1

        return collisions
