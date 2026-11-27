"""Fit Newton's law of cooling to the measured coffee temperatures.

T(t) = T_room + (T_0 - T_room) * exp(-k t)

With the room temperature known, ln(T - T_room) is a straight line in t with slope -k,
so an ordinary least-squares fit of that line gives k and T_0. Only the standard library
is needed:

    python analysis/fit_cooling.py data/coffee-cooling.csv
"""

import csv
import math
import sys

T_ROOM = 21.5  # degrees C, measured with the room thermometer (notes/lab-notes.md)


def read_measurements(path):
    """Return the times (min) and temperatures (degrees C) of the CSV file."""
    times, temps = [], []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            times.append(float(row["time_min"]))
            temps.append(float(row["temperature_C"]))
    return times, temps


def fit_line(x, y):
    """Least-squares line y = a + b x; returns a, b and the standard error of b."""
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((xi - mx) ** 2 for xi in x)
    sxy = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    b = sxy / sxx
    a = my - b * mx
    residual = sum((yi - a - b * xi) ** 2 for xi, yi in zip(x, y))
    se_b = math.sqrt(residual / (n - 2) / sxx)
    return a, b, se_b


def main(path):
    times, temps = read_measurements(path)
    log_excess = [math.log(T - T_ROOM) for T in temps]
    a, b, se_b = fit_line(times, log_excess)
    k, k_err = -b, se_b
    T0 = T_ROOM + math.exp(a)
    half_time = math.log(2) / k
    print(f"cooling constant k  = {k:.4f} +/- {k_err:.4f} 1/min")
    print(f"start temperature   = {T0:.1f} C")
    print(f"half-life of excess = {half_time:.1f} min")
    print(f"drinkable (60 C) at = {math.log((T0 - T_ROOM) / (60 - T_ROOM)) / k:.1f} min")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/coffee-cooling.csv")
