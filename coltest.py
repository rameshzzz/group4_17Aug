import numpy as np 
import pandas as pd 

if __name__=="__main__":
    df=pd.read_csv("train.csv")
    print(df.head(5))

    null_columns=df.columns[df.isnull().any()]
    x=df[null_columns].isnull().sum()
    print(x)

    #all null columns
    print(df[df.isnull().any(axis=1)][null_columns].head())

    #print column names
    list(df.columns)

