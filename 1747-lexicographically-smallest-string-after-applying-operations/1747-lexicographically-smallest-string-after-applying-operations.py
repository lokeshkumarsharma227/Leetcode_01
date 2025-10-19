from typing import Iterable


class Solution:
    def findLexSmallestString(self, S: str, a: int, b: int) -> str:
        def rot(s: str) -> str:
            return s[b:] + s[:b]

        def add(s: str) -> str:
            return ''.join(c if i % 2 == 0 else str((int(c) + a) % 10) for i, c in enumerate(s))

        seen = set()

        def dfs(s: str) -> Iterable[str]:
            yield s

            for t in [rot(s), add(s)]:
                if t not in seen:
                    seen.add(t)
                    yield from dfs(t)

        return min(dfs(S))