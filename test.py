"""
import absolute path to upload the module
"""
#DONT WORK
# import importlib.util
# path = importlib.util.spec_from_file_location("ColorPalette", "/home/ettore1461/Scrivania/ColorPalette/ColorPalette")
# cp = importlib.util.module_from_spec(path)
# path.loader.exec_module(cp)


# WORK
from importlib.machinery import SourceFileLoader
cp = SourceFileLoader("ColorPalette", "/home/ettore1461/Scrivania/ColorPalette/ColorPalette.py").load_module()

#import matplotlib.pyplot as plt
test=cp.ColorPalette(200)
tt=test._ColorPalette__palette()

#fig1 = plt.figure()
#ax1 = fig1.add_subplot(111)


from bokeh.plotting import figure, show, output_file
output_file('rectangles_rotated.html')
p = figure(plot_width=400, plot_height=400)
#test.bokeh_color(0,0,200,100,156,p)

p.rect(x=start_x+0.5, y=start_y+0.5+0.1, width=1, height=0.99, color=(200,100,150))
p.text(x=0,y=0,text="Prova")
show(p)


xdr = DataRange1d()
ydr = DataRange1d()

plot = Plot(
    title=None,
    x_range=xdr,
    y_range=ydr,
    plot_width=300,
    plot_height=300,
    h_symmetry=False,
    v_symmetry=False,
    min_border=0,
    toolbar_location=None)

glyph = Rect(x="X", y="Y", width=1, height=1, fill_color="RGB_Tuple")
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))


curdoc().add_root(plot)

show(plot)