"""
The purpose of this script is to get Bokeh up and running so that the plots can be made interactive. Drastically reducin
g the code and allowing for on the fly demonstration.
"""

"""
# Importing the relevant libraries as their usual aliases
"""

from bokeh.plotting import figure
from bokeh.models import HoverTool, Slider, ColumnDataSource
from bokeh.layouts import widgetbox, row
from bokeh.io import curdoc, output_file, show

from sklearn import datasets

import pandas as pd
import numpy as np

"""
# Loading the data set
"""
iris = datasets.load_iris()
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

print(data1.head())

for item in list(data1):
    print(item)

# Create the figure: p
plot1 = figure(title='XXX',
           x_axis_label='XXX',
           y_axis_label='XXX',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@target')]
           )
'''
plot2 = figure(title='XXX',
           x_axis_label='XXX',
           y_axis_label='XXX',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@target')]
           )
'''
# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    "SepalLength":data1["sepal length (cm)"],
    "SepalWidth":data1["sepal width (cm)"],
    "PetalLength":data1["petal length (cm)"],
    "PetalWidth": data1["petal width (cm)"],
    "target":data1["target"]
})

# Add a circle glyph to the figure p
plot1.circle(x='SepalLength', y='SepalWidth', source=source)

#plot2.circle(x='PetalLength', y='PetalWidth', source=source)

# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title="Year")

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot1)
curdoc().add_root(layout)

# Output the file and show the figure
output_file('gapminder.html')
show(layout)
