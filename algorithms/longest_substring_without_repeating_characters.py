"""
Leetcode Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def length_of_longest_substring(s: str) -> int:
    """
    :param s:
    :return:

    Skip the characters immediately when we find a repeated character.
    Reason: If s[j] have a duplicate in the range(i, j) with index j',
    we don't need to increase i little by little. We can skip all the
    elements in the range [i, j'] and let i to be j' + 1 directly.
    """
    cache = {}
    max_len = 0
    n = len(s)
    i = 0
    for j in range(n):
        if s[j] in cache.keys():
            i = max(cache[s[j]], i)
        max_len = max(max_len, j - i + 1)
        cache[s[j]] = j + 1
    return max_len


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
