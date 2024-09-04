from typing import List

import numpy as np


def calculate_overall_weekend_average(daily_weights: List[float]) -> float:
    """
    Calculate the overall weekend average.

    :param daily_weights: A list of floats representing the weights on each day.
    :return: The overall weekend average as a float.
    """
    saturdays = daily_weights[5::7]
    sundays = daily_weights[6::7]

    weekend_averages = (saturdays + sundays) / 2

    overall_average = np.mean(weekend_averages)

    return overall_average
