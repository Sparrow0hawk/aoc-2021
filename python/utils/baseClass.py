import os
import requests
import re
from aocd.models import Puzzle


class BaseChallenge(object):
    def __init__(self, day):
        self.day = day
        self.numeric_day = self._get_numeric_day()
        self.result = list()

    def _get_numeric_day(self):
        return re.findall(r"[A-Za-z]+|\d+", self.day)[-1]

    def get_data(self):
        self.data = self._get_challenge_data()
        return self.data

    def get_result(self):
        return NotImplementedError

    def return_result(self):
        return self.result

    def _get_challenge_data(self):

        puzzle = Puzzle(year=2021, day=int(self.numeric_day))

        return puzzle.input_data
