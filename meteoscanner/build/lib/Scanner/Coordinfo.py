import xarray as xr, matplotlib.pyplot as plt, numpy as np
import cartopy.crs as ccrs 
import cartopy.feature as cfeature
from matplotlib.axes import Axes

class Coordinfo:
    def  __init__(self, x, y, dataset, plotfile):
        self.x = x
        self.y = y
        self.dataset = dataset
        self.plotfile = plotfile
        self.extent = None

def fix_extent(self, extent):
    replaced_ds=self.dataset.sel(lat=slice(extent[3], extent[2]), lon=slice(extent[0], extent[1]))
    self.dataset = replaced_ds
    for i in list(replaced_ds.coords):
        if i.lower() in 'latitudes':
            self.y=replaced_ds[i].values
        elif i.lower() in 'longitudes':
            self.x=replaced_ds[i].values
        
    
        
    
