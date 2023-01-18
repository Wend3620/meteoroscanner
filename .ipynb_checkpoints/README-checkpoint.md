### visual

This notebook is dedicated for making scanning of an area by cross sections from ERA5 dataset:
<img src='Function illustration.png' width='600' height='400'/>

Such goal is achieved by the following:

First, present a base plot to choose following points by running estimation(): \
Initial start point (pos1 in the function), \
initial end point(pos2 in the function), \
and final end point(pos3 in the function).

Second, run coords_generator() to the coordinates returned earlier. 

Third, run scanner() to generate a video, whihc plays the cross sections from the starting line to the final line.

A selection function(selection()) is also defined for extracting desired dataset.

One important component of the notebook is a dictionary called <b>plotfile<\b> that includes parameter for plotting inside of the estimation() and the scanner() function.
Here is the plotfile used in the notebook:
    ```
    plotfile={'contour':{
                 'thta':{'level': np.arange(250, 450, 3),
                         'color':'red',
                         'linewidths':1,
                         'title':"Potential temperature (K)"},
                    'z':{'level': np.arange(0, 10000, 60),
                         'color':'black',
                         'linewidths':1, 
                         'title': "Geopotential height (m)"},
                    't':{'level': np.arange(0, 400, 3),
                         'color':'black',
                         'linewidths':1, 
                         'title': "Temperature (K)"}},
             'fill':{
                   'vo':{'level': np.arange(5e-5,40e-5,5e-5),
                         'cmap':plt.cm.YlOrRd,
                         'title': "Relative vorticity(1/s)"},
                    'w':{'level': np.arange(-3.5, 3.6, 0.5),
                         'cmap':plt.cm.PRGn,
                         'title': "Omega(Pa/s)"}}}
    ```
And the structure looks like such:
    <img src='plotfile.png' width='600' height='800'/>