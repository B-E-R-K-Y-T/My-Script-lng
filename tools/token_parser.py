import re

from tools.parser import get_name_and_index_indexing_array
from data.operators import ALL_OPERATORS


class TokenReader:
    def __init__(self, tokens: list):
        self.tokens = tokens

    def get_all_values_arrays(self) -> dict:
        res = {}

        for token, line, num_line in self.tokens:
            par = TokenParser(token, line)

            if par.is_operator():
                continue

            if par.is_indexing_array():
                name, index = get_name_and_index_indexing_array(token)
                res[token] = (name, index)

        return res


class TokenParser:
    def __init__(self, token: str, line: str):
        self.token = token
        self.line = line

    def is_operator(self) -> bool:
        return self.token in ALL_OPERATORS

    def is_indexing_array(self) -> bool:
        if re.findall(pattern=r'[ ]*[\w\d]+\[[\d]+\]', string=self.token):
            return True
        return False
