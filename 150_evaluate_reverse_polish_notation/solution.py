from typing import List, Union


class Solution:
    expressions = set(["*", "/", "+", "-"])

    def eval_RPN(self, tokens: List[str]) -> int:
        parts: List[int] = []

        for token in tokens:
            if token not in self.expressions:
                parts.append(int(token))
                continue

            new_val = 0
            second = int(parts.pop())
            first = int(parts.pop())
            if token == "+":
                new_val = first + second
            elif token == "-":
                new_val = first - second
            elif token == "*":
                new_val = first * second
            else:
                new_val = int(first / second)
            parts.append(new_val)

        return parts[-1]
