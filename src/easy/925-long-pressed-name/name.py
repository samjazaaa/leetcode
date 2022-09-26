
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if (len(name) > len(typed)):
            return False

        j = 0
        i = 0
        while (j < len(typed)):
            if (i < len(name) and typed[j] == name[i]):
                j += 1
                i += 1
                continue
            if (i > 0 and typed[j] == name[i-1]):
                j += 1
                continue
            return False

        if i < len(name):
            return False
        else:
            return True
