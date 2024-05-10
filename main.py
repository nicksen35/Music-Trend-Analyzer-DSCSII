import numpy as np
import pandas as pd
import statistical_analysis


data = pd.read_csv('./Data/dataset.csv')

print(data.columns.tolist())
statistical_analysis.stats_analyzer(data)
