#!/usr/bin/env python

import sys
import os 
import matplotlib
import matplotlib.pyplot as pyplot
import pylab

proactive_legend = 'ABS - ProActive backend'
java_8_legend = 'ABS - Java 8 backend'
x_legend = 'Number of workers'
y_legend = 'Computing time (s)'

# go from milliseconds to seconds
unit = 1000

matplotlib.rc('xtick', labelsize=18)
matplotlib.rc('ytick', labelsize=18)
matplotlib.rcParams.update({'font.size': 18})
 
fig, ax1 = pyplot.subplots()

#2 261436
#4 176339
#6 180106
#10 179527
#12 182884
#14 186788
#18 210183
#24 187299
#30 183338
#36 217503
#42 236362
#50 272079

x_axis=[2, 4, 6, 10, 14, 18, 24, 30, 36, 42, 50]
p1, = ax1.plot(x_axis, [364120.8/unit, 188193.4/unit, 131556.4/unit, 85341.6/unit, 67045.4/unit, 57905.8/unit, 50420.8/unit, 51683.2/unit, 56005.4/unit, 58383/unit, 75789.6/unit], linestyle='-', marker='H', color='m', linewidth=2, markersize=9)
p2, = ax1.plot(x_axis, [261436/unit, 176339/unit, 180106/unit, 179527/unit, 186788/unit, 210183/unit, 187299/unit, 183338/unit, 217503/unit, 236362/unit, 272079/unit], linestyle='-', marker='v', color='c', linewidth=2, markersize=9)

ax1.axis([1, 50, 30, 370])
ax1.set_xlabel(x_legend)
ax1.set_ylabel(y_legend)

legend1 = pyplot.legend([p1, p2], [proactive_legend, java_8_legend], loc=1, prop={'size':18})
pyplot.gca().add_artist(legend1)
pyplot.show()
