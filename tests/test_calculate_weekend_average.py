import numpy as np
import pytest

from main import calculate_overall_weekend_average


def test_calculate_overall_weekend_average():
    """
    Test case for the calculate_overall_weekend_average method.
    """
    dailywts = np.array([185, 184.8, 184.6, 184.4, 184.2, 184, 183.8,
                         183.6, 183.4, 183.2, 183, 182.8, 182.6, 182.4,
                         182.2, 182, 181.8, 181.6, 181.4, 181.2, 181,
                         180.8, 180.6, 180.4, 180.2, 180, 179.8, 179.6,
                         179.4, 179.2, 179, 178.8, 178.6, 178.4, 178.2])
    expected_overall_average = 181.1
    result = calculate_overall_weekend_average(dailywts)
    assert np.isclose(result, expected_overall_average), f"Expected {expected_overall_average}, but got {result}"


def test_empty_input():
    """
    Test the `calculate_overall_weekend_average` method with an empty input array.
    """
    dailywts = np.array([])
    expected_result = np.nan
    result = calculate_overall_weekend_average(dailywts)
    assert np.isnan(result), f"Expected {expected_result}, but got {result}"


def test_single_week():
    """
    Test the `calculate_overall_weekend_average` function with a single week of daily weights.
    """
    dailywts = np.array([185, 184.8, 184.6, 184.4, 184.2, 184, 183.8])
    expected_overall_average = 183.9
    result = calculate_overall_weekend_average(dailywts)
    assert np.isclose(result, expected_overall_average), f"Expected {expected_overall_average}, but got {result}"


def test_incomplete_week():
    """
    Test method for the calculate_overall_weekend_average function.
    It checks if the result of the calculation is NaN, given a set of daily weights incomplete.
    """
    dailywts = np.array([185, 184.8, 184.6, 184.4, 184.2, 184])
    expected_result = np.nan
    result = calculate_overall_weekend_average(dailywts)
    assert np.isnan(result), f"Expected {expected_result}, but got {result}"


def test_all_same_weight():
    """
    Test the calculate_overall_weekend_average function when all the weights are the same.
    """
    dailywts = np.array([180, 180, 180, 180, 180, 180, 180, 180, 180, 180,
                         180, 180, 180, 180, 180, 180, 180, 180, 180, 180,
                         180, 180, 180, 180, 180, 180, 180, 180, 180, 180,
                         180, 180, 180, 180, 180])
    expected_overall_average = 180.0
    result = calculate_overall_weekend_average(dailywts)
    assert np.isclose(result, expected_overall_average), f"Expected {expected_overall_average}, but got {result}"


if __name__ == "__main__":
    pytest.main()
