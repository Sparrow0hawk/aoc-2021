import os
import requests
import re


class BaseChallenge(object):
    def __init__(self, day, path):
        self.day = day
        self.path = path
        self.aoc_url = "https://adventofcode.com/2021/day/"
        self.numeric_day = self._get_numeric_day()

    def _get_numeric_day(self):
        return re.findall(r"[A-Za-z]+|\d+", self.day)[-1]

    def get_data(self):
        return self._get_challenge_data()

    def get_result(self):
        return NotImplementedError

    def return_result(self):
        return self.result

    def _get_challenge_data(self):

        response_dat = requests.get(
            f"{self.aoc_url}/{self.numeric_day}/input", stream=True
        )

        file_name = f"{self.day}.txt"

        with open(os.path.join(self.path, file_name), "wb") as data_file:
            for line in response_dat.iter_content(chunk_size=8192):
                data_file.write(line)

        return str(os.path.join(self.path, file_name))
