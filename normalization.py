from scipy.stats import mstats

def zscore_dataset(dataset):
    for column in dataset.columns:
        if dataset[column].dtype in ["int32","int64","float32","float64"]:
            dataset[column+"_zscore"] = mstats.zscore(dataset[column])
            print "z",
