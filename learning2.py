import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
from numpy import sign

perceptron = [.5, .5, -.5]
lim = 5000
df1 = pd.read_excel('data.xlsx', sheet_name=0, usecols='A', nrows=2000)
df2 = pd.read_excel('data.xlsx', sheet_name=0, usecols='B', nrows=2000)
y = df1.mean()
x = df2.mean()
pattern_yes = [y, x, 1]
#x = np.array(df1)
#y = np.array(df2)
plt.scatter(x, y)
df1 = pd.read_excel('data.xlsx', sheet_name=0, usecols='A', skiprows=2000)
df2 = pd.read_excel('data.xlsx', sheet_name=0, usecols='B', skiprows=2000)
y = df1.mean()
x = df2.mean()
pattern_no = [y, x, -0]
#x = np.array(df1)
#y = np.array(df2)
y_intercept = [0, -perceptron[2]/perceptron[1]]
x_intercept = [-perceptron[2]/perceptron[0], 0]
plt.plot(x_intercept, y_intercept)
plt.scatter(x, y)
ite = 5000
np = 2
ni = 3
alpha = 0.3
ww = [.5, .5, 1]
pat = ([pattern_yes, pattern_no])
dout =[-1, 1]
for iterations in range(0, ite):
    ou = [0, 0]
    for pattern in range(0, np):
        net = 0
        for i in range(0, ni):
            net = net + ww[i] * pat[pattern][i]

        ou[pattern] = sign(net)
        err = dout[pattern] - ou[pattern]
        learn = alpha * err
        ###
        for i in range(0, ni):
            ww[i] = ww[i] + learn * pat[pattern][i]

for i in range(0, ni):
    print(ww[i])
