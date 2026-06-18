from collections import Counter

"""Utility to check if two strings are anagrams.

This module provides a Solution class with an isAnagram method used
in algorithm practice problems.
"""


class Solution:
    """Solution container for string-related interview problems."""

    def is_anagram(self, s: str, t: str) -> bool:
        """Return True if strings s and t are anagrams of each other.

        Uses collections.Counter to compare character counts.
        """

        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter

    def is_anagram_optimized(self, s: str, t: str) -> bool:
        """Return True if s and t are anagrams using a frequency table."""
        if len(s) != len(t):
            return False

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for c in t:
            if c not in freq:
                return False

            freq[c] -= 1
            if freq[c] < 0:
                return False

        return True
# End of File