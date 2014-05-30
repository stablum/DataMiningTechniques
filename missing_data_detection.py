import pandas as pd
# detects missing data in the input pandas dataset

def run(dataset):
    dataset_value_missing = pd.isnull(dataset)
    for column in dataset_value_missing.columns:
        if True in set(dataset_value_missing[column].values):
            dataset[column+"_missing"] = dataset_value_missing[column].astype(int)
            print("m",end="",flush=True),

