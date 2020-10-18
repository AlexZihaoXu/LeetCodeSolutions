class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pairs = {}
        largest = -1
        for i, c in enumerate(s):
            if c in pairs:
                largest = max(i - pairs[c] - 1, largest)
            if c not in pairs:
                pairs[c] = i
        return largest