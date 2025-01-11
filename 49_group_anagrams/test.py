from typing import List, Tuple
import pytest
from solution import Solution


class TestGroupAnagrams:
    def __compare_lists(self, list1: List[List[str]], list2: List[List[str]]) -> bool:
        return sorted(tuple(sorted(sublist)) for sublist in list1) == sorted(
            tuple(sorted(sublist)) for sublist in list2
        )

    def test_group_anagrams(self) -> None:
        tests: List[Tuple[List[str], List[List[str]]]] = [
            (
                ["eat", "tea", "tan", "ate", "nat", "bat"],
                [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            ),
            ([""], [[""]]),
            (["a"], [["a"]]),
            (["", "", ""], [["", "", ""]]),
        ]

        for words, output in tests:
            got = Solution().group_anagrams(words)
            if not self.__compare_lists(got, output):
                pytest.fail(
                    f"Invalid result received for {words}; want={output}; got={got}!"
                )
