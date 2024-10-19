#!/usr/bin/env python3
import pandas as pd


dictionary = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four'],
}

df = pd.DataFrame(dictionary)
df = df.set_axis(['A', 'B', 'C', 'D'], axis=0)