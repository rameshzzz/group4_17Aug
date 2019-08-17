import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\ssingh3\\Desktop\\git_mini_project\\group4_17Aug\\train.csv")

def total_count(df):
    return (df.isnull().sum().sum())


if __name__ == "__main__":
    print(total_count(df))