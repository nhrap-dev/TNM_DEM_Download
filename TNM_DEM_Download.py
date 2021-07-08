#!/usr/bin/env python
# coding: utf-8

# # To run
# 1.  Update User Input Cell x and y values 
# 2.  Click the Run button

# # User Input: 

# In[2]:

import os
import requests

def TNMDem(westmostX, southmostY, eastmostX, northmostY, arcSecond):
    westmostX = abs(westmostX)
    southmostY = abs(southmostY)
    eastmostX = abs(eastmostX)
    northmostY = abs(northmostY)
    
    if eastmostX > westmostX:
        raise Exception(f"eastmostX is greater than westmostX")
    if southmostY > northmostY:
        raise Exception(f"southmostY is greater than northmostY")
    '''
    http://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/1/TIFF/
    https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1/TIFF/n19w098/USGS_1_n19w098.tif
    15 folders e instead of w, ignore for now
    '''
    dem_list = []
    
    xRange = range(int(eastmostX)+1, int(westmostX)+2)
    yRange = range(int(southmostY)+1, int(northmostY)+2)
    print(f'xRange: {xRange}')
    print(f'yRange: {yRange}')
    
    for x in xRange:
        x = f"{x:03}"
        for y in yRange:
            OneArcS=f"https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1/TIFF/n{y}w{x}/USGS_1_n{y}w{x}.tif"
            OneThirdArcS=f"https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/n{y}w{x}/USGS_13_n{y}w{x}.tif"
            if arcSecond == '1':
                dem_list.append(OneArcS)
            elif arcSecond == '13':
                dem_list.append(OneThirdArcS)
            else:
                raise Exception(f"Enter '1' for 1 arcsecond or '13' for 1/3 arcsecond, with quotation marks. You entered {arcSecond}.")
    dem_list.sort()
    return dem_list


'''USER INPUT HERE. CHANGE THESE FOUR VALUES THEN CLICK RUN'''
westmostX = -97.008
eastmostX = -95.879
northmostY = 30.792
southmostY = 29.699

'''Leave this as 1'''
arcSecond = '1' #Can be 1 for 1 arc second (Default) or 13 for 1/3 arc second.

'''This function creates the links'''
dem_list = TNMDem(westmostX, southmostY, eastmostX, northmostY, arcSecond)
print('{} DEM files found'.format(len(dem_list)))
data_folder = os.path.join(os.getcwd(), 'data')
print('DEM data will be stored at: {}'.format(data_folder))
for url in dem_list:
    data = requests.get(url)
    file_name = url.split('/')[-1]
    file_location = os.path.join(data_folder, file_name)
    with open(file_location, 'wb') as dem:
        dem.write(data.content)
print('{} files downloaded to {}'.format(len(dem_list), data_folder))