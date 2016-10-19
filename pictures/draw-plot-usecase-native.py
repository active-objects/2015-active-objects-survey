#!/usr/bin/env python

import sys
import os 
import matplotlib
import matplotlib.pyplot as pyplot
import pylab

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

p1, = ax1.plot([1, 2, 3, 5, 7, 9, 12, 15, 18, 21, 25], [364120.8/unit, 188193.4/unit, 131556.4/unit, 85341.6/unit, 67045.4/unit, 57905.8/unit, 50420.8/unit, 51683.2/unit, 56005.4/unit, 58383/unit, 75789.6/unit], linestyle='-', marker='H', color='m', linewidth=2, markersize=9)
p2, = ax1.plot([1, 2, 3, 5, 7, 9, 12, 15, 18, 21, 25], [322654.6/unit, 173963.8/unit, 121947.6/unit, 81866.8/unit, 65813.6/unit, 57362.2/unit, 50539/unit, 48441.6/unit, 47823.6/unit, 50533.6/unit, 52794.8/unit], linestyle='-', marker='v', color='c', linewidth=2, markersize=9)
p4, = ax1.plot([1, 2, 3, 5, 7, 9, 12, 15, 18, 21, 25], [261436/1000, 176339/1000, 180106/1000, 179527/1000, 186788/1000, 210183/1000, 187299/1000, 183338/1000, 217503/1000, 236362/1000, 272079/1000], linestyle='-', marker='v', color='g', linewidth=2, markersize=9)


ax1.axis([1, 25, 30, 370])
ax1.set_xlabel('Number of machines')
ax1.set_ylabel('Computing time (s)')

ax2 = ax1.twinx()
p3, = ax2.plot([1, 2, 3, 5, 7, 9, 12, 15, 18, 21, 25], [(1.1285157565-1)*100, (1.0817963277-1)*100, (1.0787944986-1)*100, (1.0424445563-1)*100, (1.0187164963-1)*100, (1.009476624-1)*100, (0.9976612121-1)*100, (1.0669176906-1)*100, (1.1710828963-1)*100, (1.1553303149-1)*100, (1.4355504709-1)*100], linestyle='--', marker='d', color='k', linewidth=2)
ax2.axis([1, 25, 0, 100])
ax2.set_ylabel('ProActive backend overhead (%)')
#for tick in ax2.get_yticklabels():
#    tick.set_color('y')

legend1 = pyplot.legend([p1, p2, p4], ['ABS-ProActive backend', 'Native ProActive', 'Java 8'], loc=2, prop={'size':18})
pyplot.legend([p3], ['Overhead'], loc=1, prop={'size':18})
pyplot.gca().add_artist(legend1)
pyplot.show()
