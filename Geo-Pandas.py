#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import osmnx as ox
from descartes import PolygonPatch
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
from pyproj import CRS


# In[39]:


yerevan = gpd.read_file(r"C:\Users\Dell\Desktop\Project\Yerevan shapefile\Yerevan.shp")
yerevan.head()


# In[40]:


yerevan.plot()


# In[41]:


yerevan.crs


# In[42]:


#Load yerevan city from openStreetMap Using oxmmnx api 
city = ox.gdf_from_place("Yerevan , Armenia")
print(city.crs)
city = ox.projection.project_gdf(city)
fig, ax = ox.plot_shape(city)
print(city.crs)


# In[43]:


city.to_file(r'C:\Users\Dell\Desktop\Project\Yerevan shapefile\city.shp')


# In[44]:


geometry = city['geometry'].iloc[0]
print(type(geometry))


# In[45]:


geometry_cut = ox.quadrat_cut_geometry(geometry, quadrat_width = 750)
print(type(geometry_cut))


# In[46]:


polylist = [p for p in geometry_cut]

#Plot city

west , south , east , north = city.unary_union.bounds
fig, ax = plt.subplots(figsize=(40,40))
for polygon, n in zip(geometry_cut, np.arange(len(polylist))):
    p = polygon.representative_point().coords[:][0]
    patch = PolygonPatch(polygon, fc = '#ffffff', ec = '#000000',alpha = 0.5, zorder = 2)
    ax.add_patch(patch)
    plt.annotate(s=n, xy=p, horizontalalignment='center', size = 15)

ax.set_xlim(west,east)
ax.set_ylim(south,north)
ax.axis('off')
plt.show()


# In[33]:


np.arange(len(polylist))


# In[ ]:




