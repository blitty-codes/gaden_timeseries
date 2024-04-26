from typing import List

import numpy as np
import pandas as pd


class Pipeline:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
        self.combined_df: pd.DataFrame = None

    def process(self) -> pd.DataFrame:
        timestamps = self.data["timestamp"]
        columns = [
            "light_air",
            "moisture_ground",
            "dht_air_humidity",
            "dht_air_temperature",
            "dht_ground_humidity",
            "dht_ground_temperature",
        ]
        indexes = self.__fix_missing_vaues(timestamps)
        dataframe = self.__add_missing_values(indexes)
        dataframe = self.__detrend(dataframe, columns, 30)
        dataframe = self.__scale(dataframe, columns)

        return dataframe

    def __fix_missing_vaues(self, timestamps: np.ndarray):
        """
        Return array of indexes where values are missing between that index and next.
        """
        t = int(timestamps[0])
        c = 0
        indexes = []
        for i, timestamp in enumerate(timestamps[1:]):
            diff = int(timestamp) - t
            t = int(timestamp)

            # missing data from sensors
            # at least one timestamp is missing
            if diff >= 60:
                indexes.append(i)
                c += diff // 30

        print(f"[+] Total missing values: {c}")

        return indexes

    def __add_missing_values(self, indexes) -> pd.DataFrame:
        """
        Creates a new pandas dataframe with the new values added.
        """

        # Assuming indexes and timestamps are defined somewhere in your code
        cols = self.data.columns
        timestamps = self.data["timestamp"]
        new_data = []

        for index in indexes:
            diff = timestamps[index + 1] - timestamps[index]
            n_values = diff // 30

            if n_values > 0:
                # nan_values = np.full((n_values, len(cols)), np.nan)
                for i in range(n_values):
                    value = [np.nan] * len(cols)
                    value[0] = timestamps[index] + (i + 1) * 30
                    new_data.append(value)

        new_data_df = pd.DataFrame(new_data, columns=cols)
        combined_df = pd.concat([self.data, new_data_df], ignore_index=True)

        combined_df.sort_values("timestamp", inplace=True)
        combined_df.reset_index(drop=True, inplace=True)

        # resolve NaN values
        for col in combined_df.columns:
            combined_df[col] = combined_df[col].interpolate()

        # change moisture for mean of moisture
        # this is because there was a problem with the sensor
        # and the data is inconsistent
        moving_avg = combined_df["moisture_ground"].rolling(window=30).mean()
        combined_df.drop(columns=["moisture_ground"])
        combined_df["moisture_ground"] = moving_avg

        return combined_df

    def __detrend(
        self, data: pd.DataFrame, columns: List[str], window_size: int
    ) -> pd.DataFrame:
        """
        Detrend columns use wants.
        """
        detrended_df = pd.DataFrame()
        for col in columns:
            moving_avg = data[col].rolling(window=window_size).mean()
            detrended_ts = data[col] - moving_avg
            detrended_df[col] = detrended_ts

        detrended_df["timestamp"] = data["timestamp"]
        # get rid of first 30 values because no trend can be calculated thus is filled with NaN values
        detrended_df = detrended_df.dropna()

        return detrended_df

    def __scale(self, data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        scale (0, 1)
        """
        scaled_df = pd.DataFrame()
        for col in columns:
            # scaling values
            min_val = data[f"{col}"].min()
            max_val = data[f"{col}"].max()
            scaled_series = (data[f"{col}"] - min_val) / (max_val - min_val)
            scaled_df[col] = scaled_series

        scaled_df["timestamp"] = data["timestamp"]

        return scaled_df
