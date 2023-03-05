# use stringio to import the data from the data.txt file
from io import StringIO

from matplotlib import pyplot as plt

import scipy.optimize as opt
import numpy as np
import math

plt.rcParams['figure.figsize'] = [12, 9]

datafile = StringIO("""\
25	217
24	214
23	220
22	220
21	227
20	236
19	250
18	270
17	290
16	310
15	345
14	375
13	400
12	425
11	460
10	515
09	545
08	580
07	615
""")

data_x, data_y = np.loadtxt(datafile, unpack=True)

print(data_x)
print(data_y)


# define objective function

def objective(x, a, b):
    return a / (x + b)


# fit curve

popt, _ = opt.curve_fit(objective, data_x, data_y, p0=[5000, 1], method="trf", verbose=2)

# summarize the parameter values

a, b = popt

print('a=%.3f, b=%.3f' % (a, b))

# scatter plot of the data

plt.scatter(data_x, data_y)

# draw the fitted curve

x_line = np.arange(min(data_x), max(data_x), 1)
y_line = objective(x_line, a, b)
plt.plot(x_line, y_line, '--', color='red')
# label y axis to längd (mm)
plt.ylabel('längd (mm)')
# label x axis to tid (s)
plt.xlabel('tid (s)')
# Name the graph
plt.title('Förhållande mellan tid och längd')
plt.show()
