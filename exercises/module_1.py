#!/usr/bin/env python3
"""
Exercises - Module 1
"""

from __future__ import print_function
import pandas as pd


def panda_version():
    """Print the version of panda"""
    print('panda version: ', pd.__version__)

def california_housing_stats():
    """Print stats extracted from a CSV file about California housing.
        The CSV file is coming from a remote resource."""

    california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
    stats = california_housing_dataframe.describe()
    print(stats)
