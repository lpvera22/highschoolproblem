# Weekend Average Weight Calculator

This Python function, `calculate_overall_weekend_average`, computes the average weights recorded on weekends (Saturday and Sunday) from a list of daily weight measurements. It is designed to extract and average the weights for Saturdays and Sundays, and then calculate the overall average weekend weight across all weekends provided in the data.

## Function Overview

### `calculate_overall_weekend_average(daily_weights: List[float]) -> float`

### Parameters:
- `daily_weights` (`List[float]`): A list of floating-point numbers representing daily weights. It is assumed that the list starts on a Monday and follows the order of days (in other words, Monday to Sunday). Each entry corresponds to a day's weight.

### Returns:
- A floating-point number representing the overall average of the weights on weekends (Saturdays and Sundays) across all available weekends in the input list.

### How it Works:
1. The function slices the input list `daily_weights` to extract the weights recorded on Saturdays (index 5 in a week) and Sundays (index 6 in a week).
2. It averages the weights for each weekend (Saturday and Sunday).
3. Finally, it returns the overall average of all the weekend averages calculated.

### Usage
```python
# Example daily weights for two weeks (starting on Monday)
daily_weights = [70.0, 69.5, 70.2, 70.1, 69.8, 70.3, 70.5,  # First week
                 70.1, 69.9, 70.4, 70.0, 69.7, 70.2, 70.6]  # Second week

average_weekend_weight = calculate_overall_weekend_average(daily_weights)
print(f"Overall weekend average: {average_weekend_weight}")
```
### Requirements:
1. Python 3.x
2. Numpy

### Notes:
1. The input list daily_weights must contain weights for full weeks (in other words, multiples of 7 days) to accurately compute weekend averages.
2. If the list doesn't start on a Monday, the indexes for Saturday and Sunday will not be correct.

### Future Improvements:
- Add error handling for cases where the list length is not a multiple of 7.
- Allow customization of the week start day for more flexibility.