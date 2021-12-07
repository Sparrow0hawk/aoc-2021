from utils.baseClass import BaseChallenge
import utils
import pandas as pd


class Challenge(BaseChallenge):
    def __init__(self, day):
        super().__init__(day)

    def get_result(self):
        # split the data by newline
        data_list = self.data.split("\n")

        data_list = [int(val) for val in data_list]

        # load data into dataframe
        df = pd.DataFrame.from_dict({"data": data_list})
        # create a boolean mask array based on
        # difference between original dataframe and the shifted dataframe
        # if value is greater than zero means it has increased
        shift_mask = (df - df.shift()) > 0

        # set self.result based on sum of boolean array
        self.result = shift_mask.sum().tolist()[0]

        return self.result
