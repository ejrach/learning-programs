# Making a basic Bokeh Line graph

#importing bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#prepare the output file
output_file("Line.html")

#create a figure object
f=figure()

#create line plot
#f.line(x,y)

#triangle glyphs
#f.triangle(x,y)

#circle glyphs
f.circle(x,y)



show(f)