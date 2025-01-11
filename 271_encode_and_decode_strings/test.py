from typing import List, Tuple
import pytest
from solution import Solution


class TestEncodeDecodeStrings:
    __delimiter = "a"

    def test_encode(self) -> None:
        tests: List[Tuple[List[str]], str] = [
            (
                ["neet", "code", "love", "you"],
                f"4{self.__delimiter}neet4{self.__delimiter}code4{self.__delimiter}love3{self.__delimiter}you",
            ),
            (
                ["we", "say", ":", "yes"],
                f"2{self.__delimiter}we3{self.__delimiter}say1{self.__delimiter}:3{self.__delimiter}yes",
            ),
            ([], ""),
        ]

        for str_input, want in tests:
            got = Solution().encode(str_input)
            assert want == got

    def test_decode(self) -> None:
        tests: List[Tuple[str, List[str]]] = [
            (
                f"4{self.__delimiter}neet4{self.__delimiter}code4{self.__delimiter}love3{self.__delimiter}you",
                ["neet", "code", "love", "you"],
            ),
            (
                f"2{self.__delimiter}we3{self.__delimiter}say1{self.__delimiter}:3{self.__delimiter}yes",
                ["we", "say", ":", "yes"],
            ),
            ("", []),
        ]

        for input_str, want in tests:
            got = Solution().decode(input_str)
            if sorted(got) != sorted(want):
                pytest.fail(
                    f"Invalid result received for {input_str}; want={want}; got={got}!"
                )
