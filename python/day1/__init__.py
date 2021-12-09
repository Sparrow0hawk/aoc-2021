from utils.baseClass import BaseChallenge
import utils
import pandas as pd


class Challenge(BaseChallenge):
    def __init__(self, day):
        super().__init__(day)

    def _get_data_df(self):
        """
        A function for loading the data splitting it and creating a
        pandas.DataFrame with a single `data` column
        """
        # split the data by newline
        data_list = self.data.split("\n")

        data_list = [int(val) for val in data_list]

        # load data into dataframe
        self.df = pd.DataFrame.from_dict({"data": data_list})

        return self.df

    def get_result(self):

        df = self._get_data_df()

        # create a boolean mask array based on
        # difference between original dataframe and the shifted dataframe
        # if value is greater than zero means it has increased
        shift_mask = (df - df.shift()) > 0

        # set self.result based on sum of boolean array
        self.result.append(f"Part 1: {shift_mask.sum().tolist()[0]}")

        return self.result

    def get_part2(self):
        """
        Solution for part 2, using a 3-wide sliding window
        """

        df = self._get_data_df()

        window_df = df.rolling(3).sum()

        shift_mask = (window_df - window_df.shift(1)) > 0

        self.result.append(f"Part 2: {shift_mask.sum().tolist()[0]}")

        return self.result
