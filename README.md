# line-fit-cli

<!-- [![License](https://img.shields.io/pypi/l/line-fit-cli.svg?color=green)](https://github.com/ianhi/line-fit-cli/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/line-fit-cli.svg?color=green)](https://pypi.org/project/line-fit-cli)
[![Python Version](https://img.shields.io/pypi/pyversions/line-fit-cli.svg?color=green)](https://python.org)
[![CI](https://github.com/ianhi/line-fit-cli/actions/workflows/ci/badge.svg)](https://github.com/ianhi/line-fit-cli/actions)
[![codecov](https://codecov.io/gh/ianhi/line-fit-cli/branch/master/graph/badge.svg)](https://codecov.io/gh/ianhi/line-fit-cli) -->

cli for loading csvs and fitting simple curves to them. Avoid opening needing to open a full python session or excel.

Standard Least squares with a plot
```bash
csv-fit-linear examples/example.csv
```

Without a plot
```bash
csv-fit-linear examples/example.csv --no-plot
```


Ridge Regression

```bash
csv-fit-linear examples/example.csv --ridge
```

Ridge regression changing alpha
```bash
csv-fit-linear examples/example.csv --ridge --ridge-alpha=.5
```

