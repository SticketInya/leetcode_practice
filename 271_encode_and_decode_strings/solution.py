from typing import List


class Solution:
    __DELIMITER = "a"

    def encode(self, strs: List[str]) -> str:
        output: str = ""
        if not strs:
            return output

        for word in strs:
            output += f"{len(word)}{self.__DELIMITER}{word}"

        return output

    def decode(self, s: str) -> List[str]:
        output: List[str] = []
        if s == "":
            return output

        current_buff: str = ""
        i = 0
        while i < len(s):
            if s[i] != self.__DELIMITER:
                current_buff += s[i]
                i += 1
                continue

            text_len: int = int(current_buff)
            next_start: int = text_len + 1
            text: str = s[i + 1 : i + next_start]

            output.append(text)
            i += next_start
            current_buff = ""

        return output

    # def decode(self, s: str) -> List[str]:
    #     output: List[str] = []
    #     if s == "":
    #         return output

    #     parts = s.split(self.__DELIMITER)
    #     for i in range(len(parts) - 1):
    #         text_length = int(parts[i], base=10)
    #         text = parts[i + 1][:text_length]
    #         parts[i + 1] = parts[i + 1][text_length:]
    #         output.append(text)

    #     return output
