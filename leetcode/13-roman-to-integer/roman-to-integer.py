class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        
        total = 0
        i = 0

        while i < len(s):
            curr = values[s[i]]
            if i + 1 < len(s) and curr < values[s[i + 1]]:
                total += values[s[i + 1]] - curr
                i += 2
            else:
                total += curr
                i += 1

        return total