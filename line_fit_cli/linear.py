import numpy as np

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None
from sklearn import linear_model
from typing import Sequence


def fit(file: Sequence[str], delim: str, plot: bool):
    data = np.genfromtxt(file[0], delimiter=delim)
    reg = linear_model.LinearRegression()
    reg.fit(data[:, 0][:, None], data[:, 1])
    print(f"slope={reg.coef_[0]:.4f}")
    print(f"intercept={reg.intercept_:.4f}")
    if plt is not None and plot:
        fig, ax = plt.subplots()
        ax.plot(data[:, 0], data[:, 1], "o")
        ax.plot(data[:, 0], reg.predict(data[:, 0][:, None]), "-")
        plt.show()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Linear fit of csv file")
    parser.add_argument("file", nargs=1)
    parser.add_argument(
        "-d",
        "--delimiter",
        type=str,
        default=" ",
        help="delimiter of csv file. e.g. ' '  or ," f"(default: space)",
    )
    parser.add_argument(
        "--plot",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="Whether to make and show a plot.",
    )
    args = parser.parse_args()
    fit(args.file, args.delimiter, args.plot)
