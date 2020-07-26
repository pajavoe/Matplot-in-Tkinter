#
from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg, NavigationToolbar2Tk #sometimes also NavigationToolbar2TkAgg 
from matplotlib.figure import Figure
import tkinter as tk
import matplotlib


xar = []
yar = []
zar = []
def animate(i): # updating new points - change xar,yar,zar to needed values
            #print(i)
            yar.append(99-i)
            xar.append(i)
            zar.append(50)
            
            GraphPage.line.set_data(yar,xar) 
            GraphPage.line.set_3d_properties(zar)
            
class GraphPage(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.title_label = tk.Label(self, text="Graph Page Example")
        self.title_label.pack()
        self.pack()

    def add_mpl_figure(self, fig):
        
        
        self.mpl_canvas = FigureCanvasTkAgg(fig, self)
        #self.mpl_canvas.show()
        
        self.mpl_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        #adds toolbar -
        self.toolbar = NavigationToolbar2Tk(self.mpl_canvas, self)#sometimes also NavigationToolbar2TkAgg 
        self.toolbar.update()
        ax = fig.get_axes()[0]
        Axes3D.mouse_init(ax) # enable 3d mouse drag
        #-
    
        self.mpl_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        


class MPLGraph(Figure):
    
    def __init__(self):
        Figure.__init__(self, figsize=(5, 5), dpi=100)
        self.plot = self.add_subplot(111,projection='3d')#projection='3d' for 3d view
        #sets limit of axis 
        self.plot.set_ylim(0, 100)
        self.plot.set_xlim(0, 100)
        self.plot.set_zlim(0, 100)
        #self.plot.plot([1, 2, 3, 4, 5, 6, 7], [4, 3, 5, 0, 2, 0, 6],[7, 3, 5, 4, 2, 8, 6])
        GraphPage.line, = self.plot.plot(xar, yar, zar) #plots the line


fig = MPLGraph()

root = tk.Tk()
graph_page = GraphPage(root)
graph_page.add_mpl_figure(fig)
ani = animation.FuncAnimation(fig, animate, interval=100, blit=False) # animates

root.mainloop()
