from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack: List[str] = []
        combinations: List[str] = []

        def backtrack(opened: int, closed: int) -> None:
            if len(stack) == n * 2:
                combinations.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)

        return combinations

    def generateParenthesisDFS(self, n: int) -> List[str]:
        def dfs(open_count: int, closed_count: int, s: str) -> List[str]:
            if len(s) == n * 2:
                return [s]

            res = []
            if open_count < n:
                res += dfs(open_count + 1, closed_count, s + "(")

            if open_count > closed_count:
                res += dfs(open_count, closed_count + 1, s + ")")

            return res

        return dfs(0, 0, "")
