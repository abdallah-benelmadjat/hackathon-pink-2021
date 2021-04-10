import csv
import numpy as np
import pandas as pd
Mat = [ np.zeros(4),
        np.zeros(4),
        np.zeros(4),
        np.zeros(4)
    ]
# Mat = []

with open('test.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    i=0 
    for row in reader:
        if 'a' in row:
        	Mat[i][0] = 1
        if 'b' in row:
        	Mat[i][1] = 1
        if 'c' in row:
        	Mat[i][2] = 1
        if 'd' in row:
        	Mat[i][3] = 1
        i=i+1

print(pd.DataFrame(Mat))
pd.DataFrame(Mat).to_csv("file.csv")
