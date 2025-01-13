from typing import List, Tuple, Union
import pytest
from solution import MinStack


class TestMinStack:

    def test_min_stack(self) -> None:
        tests: List[Tuple[List[str], List[List[int]], List[Union[int, None]]]] = [
            (
                ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[], [-2], [0], [-3], [], [], [], []],
                [None, None, None, None, -3, None, 0, -2],
            ),
        ]

        for calls, parameters, want in tests:
            # Initialize stack
            min_stack = MinStack()
            results = []

            # Execute each operation
            for i, call in enumerate(calls):
                if call == "MinStack":
                    results.append(None)
                elif call == "push":
                    results.append(min_stack.push(parameters[i][0]))
                elif call == "pop":
                    results.append(min_stack.pop())
                elif call == "top":
                    results.append(min_stack.top())
                elif call == "getMin":
                    results.append(min_stack.get_min())

            # Assert results match expected output
            assert results == want, f"Expected {want}, but got {results}"
