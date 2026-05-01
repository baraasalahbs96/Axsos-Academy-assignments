class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        values = list(freq.values())
        return all(v == values[0] for v in values)