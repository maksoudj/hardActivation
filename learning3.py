import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def sign (net):
    if net >= 0:
        return 1
    else:
        return 0

def printdata (iteration, pattern, net, err, learn, ww):
    ww_formatted = ['%.2f' % elem for elem in ww]
    print("ite= ", iteration, ' pat= ', pattern, 'net= ', round(net, 5), 'err= ', err, 'lrn= ', learn,
          'weights= ', ww_formatted)

ite = 100
np = 3000
ni = 3
alpha = .01
ww = numpy.random.uniform(size=ni, low=-0.5, high=0.5)
print(ww)
df1 = pd.read_excel('data.xlsx', sheet_name=0, usecols='A:C', nrows=2000, header=None)
df2 = pd.read_excel('data.xlsx', sheet_name=0, usecols='A:C', nrows=2000, header=None, skiprows=2000)
pat = pd.read_excel('data.xlsx', sheet_name=0, usecols='A:C', nrows=4000, header=None)
pat, test = train_test_split(pat, train_size=.75, test_size=.25)
pat.reset_index(drop=True, inplace=True)
test.reset_index(drop=True, inplace=True)
dout = (pat[2])
TE = 0.0
for iterations in range(0, ite):
    ou = []

    for pattern in range(0, np):
        net = 0
        for i in range(0, ni):
            net = net + ww[i] * pat[i][pattern]
        ou.insert(pattern, sign(net))
        err = dout[pattern] - ou[pattern]
       # TE += err
       # if (.0001 > err > 0) or (-.0001 < err < 0):
        #    break
        TE += (err)**2
        if TE <= 0.0001:
            break
        learn = alpha * err
       # printdata(ite, pat, net, err, learn, ww)
        for i in range(0, ni):
            ww[i] = ww[i] + learn * pat[i][pattern]
    
    TE = 0.0

plt.scatter(df1[1], df1[0])
plt.scatter(df2[1], df2[0])
#plt.plot()
xint = (-ww[2] / ww[1], 0)
yint = (0, -ww[2] / ww[0])
plt.plot(xint, yint)
plt.show()
print(ww)




