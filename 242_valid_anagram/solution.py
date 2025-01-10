class Solution(object):
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter: dict[str, int] = {}
        t_counter: dict[str, int] = {}

        for i, _ in enumerate(s):
            if s[i] not in s_counter:
                s_counter[s[i]] = 0
            if t[i] not in t_counter:
                t_counter[t[i]] = 0
            s_counter[s[i]] = s_counter[s[i]] + 1
            t_counter[t[i]] = t_counter[t[i]] + 1

        for letter, count in s_counter.items():
            if not t_counter.get(letter) or t_counter[letter] != count:
                return False

        return True
