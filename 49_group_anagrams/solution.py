from typing import Dict, List


class Solution(object):
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        seen: Dict[str, List[str]] = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:
                seen[sorted_word] = [word]

        return seen.values()
