from typing import List, Tuple
from solution import TimeMap


class TestTimeBasedKeyValueStore:

    def testTimeMap(self):
        tests: List[Tuple[List[str], List[Tuple[str, str, int]], List[str | None]]] = [
            (
                ["TimeMap", "set", "get", "get", "set", "get", "get"],
                [
                    [],
                    ["foo", "bar", 1],
                    ["foo", 1],
                    ["foo", 3],
                    ["foo", "bar2", 4],
                    ["foo", 4],
                    ["foo", 5],
                ],
                [None, None, "bar", "bar", None, "bar2", "bar2"],
            ),
            (
                ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
                [
                    [],
                    ["love", "high", 10],
                    ["love", "low", 20],
                    ["love", 5],
                    ["love", 10],
                    ["love", 15],
                    ["love", 20],
                    ["love", 25],
                ],
                [None, None, None, "", "high", "high", "low", "low"],
            ),
        ]

        for operations, inputs, expected in tests:
            time_map = TimeMap()
            results = [None]  # First result for TimeMap initialization

            for i in range(1, len(operations)):
                operation = operations[i]
                current_input = inputs[i]

                if operation == "set":
                    time_map.set(current_input[0], current_input[1], current_input[2])
                    results.append(None)
                elif operation == "get":
                    result = time_map.get(current_input[0], current_input[1])
                    results.append(result)

            assert (
                results == expected
            ), f"Test case failed! Expected {expected}, but got {results}"
