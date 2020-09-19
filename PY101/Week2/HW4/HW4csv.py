import pandas as pd
#data file location
filenm = "/opt/miniconda3/envs/PY101/Week2/HW4/trafficdata.csv"
#read in csv file and encode info as latin
data = pd.read_csv(filenm, encoding="latin1")
#prints mean, median, and mode
print("MEAN")
print(data.mean(), "\n")
print("MEDIAN")
print(data.median(), "\n")
print("MODE")
print(data.mode())
