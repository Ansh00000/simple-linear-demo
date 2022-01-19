import numpy as np
import DataClass as dc
import matplotlib.pyplot as plt
import prints as prnt

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression