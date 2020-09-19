#Problem 2/JSON File
import pandas as pd
import json
#data file location
filenm = "/opt/miniconda3/envs/PY101/Week2/HW4/Hawaii.json"
#open file
with open(filenm) as agr_data:
    data = json.load(agr_data)
#find data
print(data.keys())
#what type form is data
print(type(data['data']))
#Last 3 columns (have numbers)
data_info = pd.DataFrame(data['data'])
data_numinfo = data_info.iloc[:,-3:]
#find mean, median, mode
print("MEAN")
print(data_numinfo.mean(), "\n")
print("MEDIAN")
print(data_numinfo.median(), "\n")
print("MODE")
print(data_numinfo.mode())

#spent hours trying to find json file with numerical data and gave up!
#so I used your hawaii data...
