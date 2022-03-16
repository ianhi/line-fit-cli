import numpy as np

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None
from sklearn import linear_model
from typing import Sequence


def _plot(data, reg):
    if plt is not None:
        fig, ax = plt.subplots()
        ax.plot(data[:, 0], data[:, 1], "o")
        ax.plot(data[:, 0], reg.predict(data[:, 0][:, None]), "-")
        plt.show()
def _print(reg):
    """Print out regression information in a nice way
    TODO: make it actually nice"""
    print(reg)
    print(f"slope={reg.coef_[0]:.4f}")
    print(f"intercept={reg.intercept_:.4f}")

def fit(file: Sequence[str], delim: str, plot: bool, ridge: bool=False, ridge_alpha: float=1):
    data = np.genfromtxt(file[0], delimiter=delim)
    if ridge:
        model = linear_model.Ridge(ridge_alpha)
    else:
        model = linear_model.LinearRegression()
    model.fit(data[:, 0][:, None], data[:, 1])
    _print(model)
    if plot:
        _plot(data, model)

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
    parser.add_argument(
        "--ridge",
        action="store_true",
        default=False,
        help="If passed then perform a ridge regression"
    )
    parser.add_argument(
        "--ridge-alpha",
        default=1,
        help="The regularization value for Ridge regression"
    )
    args = parser.parse_args()
    fit(args.file, args.delimiter, args.plot, args.ridge, args.ridge_alpha)
