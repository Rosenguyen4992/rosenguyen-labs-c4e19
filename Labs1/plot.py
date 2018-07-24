import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#1. Prepare data
labels = ["iOS", "Android", "Web", "React Native"]
values = [15, 15, 40, 30]
colors = ["green", "red", "yellow", "brown"]
explode = [0.1, 0.1, 0, 0.15]

#2. Plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode)
pyplot.axis("equal")

#3. Show
pyplot.show()