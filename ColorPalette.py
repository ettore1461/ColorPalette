



class ColorPalette:
    """
    This class create a color palette in RGB
    """

    __slots__ = ["minRGB","maxRGB","RGB_array","height","width"]

    def __init__(self, N=20):
        """
        Inizialize the istance variable
        :param N: number of elements between 0 and 255
        """
        self.minRGB=0
        self.maxRGB=255

        self.RGB_array=range(self.minRGB,self.maxRGB+1,N)
        self.height=0.6 #altezza totale, scritta + rettangolo
        self.width=0.5 #larghezza rettangolo




    def __palette(self):
        result=[]

        for R in self.RGB_array:
            for G in self.RGB_array:
                for B in self.RGB_array:
                    result=result+[[R,G,B]]


        return result

    def draw_palette(self,save_path=None):
        import matplotlib.pyplot as plt
        import numpy as np
        from math import ceil

        palettes=self.__palette()

        n_col=15 # column number
        n_row=ceil(np.shape(palettes)[0]/n_col)


        width=[i*self.width for i in range(0,n_col+1,1)]
        height = [i * self.height for i in range(0, n_row + 1, 1)]

        X,Y =np.meshgrid(width,height) # create the grid of all points

        X = X.reshape(X.size) # array of X coordinates
        Y = Y.reshape(Y.size) # array of Y coordinates

        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.xlim(0,(n_col+1)*self.width)
        plt.ylim(0,(n_row+1)*self.height)

        for i in range(0,np.shape(palettes)[0]):
            self.draw_color(X[i],Y[i],palettes[i][0],palettes[i][1],palettes[i][2],ax)

        if save_path==None:
            plt.show()
        else:
            plt.savefig(save_path,dpi=300)


    def Bokeh_palette(self):
        from bokeh.plotting import figure, show, output_file
        output_file('rectangles.html')
        p = figure(plot_width=1820, plot_height=800)

        Data=self.Plotting_Data()

        for i in range(0,Data.shape[0]):

            temp=Data.iloc[i,:]
            p.rect(x=temp["X"] + 0.5, y=temp["Y"] + 0.5 + 0.1
                   , width=self.width, height=self.height
                   , color=temp["RGB_Tuple"])
            #p.text(x=temp["X"], y=temp["Y"], text="Prova")

        show(p)



    def RGB_Text(self,R,G,B):
        return "R:{0}\nG:{1}\nB:{2}".format(R, G, B)

    def Plotting_Data(self):
        from pandas import DataFrame
        from numpy import meshgrid,shape

        from math import ceil

        # RGB Data
        X,Y,Z= meshgrid(self.RGB_array,self.RGB_array,self.RGB_array)
        X=X.reshape(X.size)
        Y=Y.reshape(Y.size)
        Z=Z.reshape(Z.size)

        Data=DataFrame({"R":X,"G":Y,"B":Z})

        # Text Data
        Data["Text"]=[self.RGB_Text(Data["R"][i],Data["G"][i],Data["B"][i]) for i in range(0,Data.shape[0])]
        Data["RGB_Tuple"] = [(Data["R"][i], Data["G"][i], Data["B"][i]) for i in range(0, Data.shape[0])]

        # Position Data
        n_col = 15
        n_row = ceil(shape(Data["R"])[0] / n_col)

        col=[i * self.width for i in range(0,n_col+1)]
        row=[i * self.height for i in range(0,n_row+1)]

        X, Y = meshgrid(col,row)

        X = X.reshape(X.size)
        Y = Y.reshape(Y.size)

        Data["X"] = X[0:shape(Data["R"])[0]]
        Data["Y"] = Y[0:shape(Data["R"])[0]]

        return Data

    def Bokeh_Data(self):
        from bokeh.models import ColumnDataSource

        return ColumnDataSource(self.Plotting_Data())


    def bokeh_color(self,start_x, start_y,R,G,B,fig):
        from bokeh.plotting import figure, show, output_file
        fig.rect(x=start_x+0.5, y=start_y+0.5+0.1, width=1, height=0.99, color=(R, G, B))
        #Text = "R:{0}\nG:{1}\nB:{2}".format(R, G, B)
        #fig.text(x=start_x,y=start_y,text="Prova")








    def draw_color(self,start_x, start_y,R,G,B,axis=None):
        """
        draw a single color with annotation
        :param start_x:
        :param start_y:
        :param R: number between 0 and 255
        :param G: number between 0 and 255
        :param B: number between 0 and 255
        :return:
        """
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches

        if axis==None:

            return patches.Rectangle((start_x, start_y),  # (x,y)
                self.width,  # width
                self.height,  # height
                color=[R/255,G/255,B/255]
            )
        else:
            #alignment = {'horizontalalignment': 'left', 'verticalalignment': 'center'}
            axis.add_patch(patches.Rectangle((start_x, start_y+0.1),  # (x,y)
                              self.width,  # width
                              self.height-0.1,  # height
                              color=[R / 255, G / 255, B / 255]))

            Text="R:{0}\nG:{1}\nB:{2}".format(R,G,B)
            #axis.text(start_x, start_y+0.05,Text,style='italic',weight='bold',size=5)

