import numpy as np
import pandas as pd


def log10(values):
    """
    Calculate log10 of given values.
    The non-positive values will be converted to be one magnitude smaller than the smallest positive value.
    """
    if not isinstance(values, pd.Series):
        values = pd.Series(values)
    positive_idx = values > 0
    min_value = values[positive_idx].min()
    values_log10 = values.copy()
    values_log10[positive_idx] = np.log10(values[positive_idx])
    values_log10[~positive_idx] = np.floor(np.log10(min_value)) - 1
    return values_log10


def get_log10_ticks(values):
    """
    Get log10 ticktext and tickvals of given values.
    """
    if not isinstance(values, pd.Series):
        values = pd.Series(values)
    positive_idx = values > 0
    min_value = values[positive_idx].min()
    max_value = values[positive_idx].max()
    max_value = np.ceil(np.log10(max_value))
    min_value = np.floor(np.log10(min_value))
    ticktext = [y * 10 ** x for x in range(int(min_value), int(max_value)) for y in range(1, 10)] + [10 ** max_value]
    tickvals = np.log10(np.array(ticktext))
    for i, x in enumerate(ticktext):
        # Use space instead of empty string.
        # Because empty string causes plot to shrink when used on y-axis of scatter plot.
        ticktext[i] = " " if i % 9 != 0 else x

    if not all(positive_idx):
        tickvals = np.insert(tickvals, 0, min_value - 1)
        ticktext = ["NA"] + ticktext
    return ticktext, tickvals
