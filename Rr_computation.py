import numpy as np
import pandas as pd

# Simple implementation of a response–recovery Hot Moment framework.
# In general, response (R) represents the magnitude of system deviation within a window,
# and recovery (r) represents the time required for the system to return toward its previous state.
# In this implementation:
# R = absolute relative change between baseline ("before") and window end ("after"). 
#       A tolerance (epsilon) is used to avoid division by zero, a valid value for SPCOND data.
# r = time until signal returns within a tolerance (max_change) of baseline; otherwise NaT.

def compute_response_recovery(
    df,
    parameters,
    window_length,
    step,
    epsilon=1e-9, # To avoid dividing by zero
    max_change=0.15
):
    results = []
    df = df.sort_index()

    for param in parameters:
        if param not in df.columns:
            continue

        series = df[param].dropna()
        if len(series) < 2:
            continue

        index = series.index
        values = series.values

        start_time = index.min()
        end_time = index.max() - window_length

        current_times = pd.date_range(start_time, end_time, freq=step)

        for current in current_times:

            after_time = current + window_length

            before_idx = index.searchsorted(current)
            after_idx = index.searchsorted(after_time)

            if before_idx >= len(values) or after_idx >= len(values):
                continue

            before = values[before_idx]
            after = values[after_idx]

            if np.isnan(before) or np.isnan(after):
                continue

            response = abs((before - after) / (before + epsilon))

            future_vals = values[after_idx+1:]
            future_times = index[after_idx+1:]

            if len(future_vals) == 0:
                recovery_time = pd.NaT
            else:
                diffs = np.abs(future_vals - before) / (before)
                recovery_mask = diffs <= max_change

                if recovery_mask.any():
                    recovered_idx = np.argmax(recovery_mask)
                    recovery_time = future_times[recovered_idx] - index[after_idx]
                else:
                    recovery_time = pd.NaT

            results.append({
                "parameter": param,
                "start_time": current,
                "before": before,
                "after": after,
                "response": response,
                "recovery": recovery_time
            })

    return pd.DataFrame(results)