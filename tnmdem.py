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
    list = []
    
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
                list.append(OneArcS)
            elif arcSecond == '13':
                list.append(OneThirdArcS)
            else:
                raise Exception(f"Enter '1' for 1 arcsecond or '13' for 1/3 arcsecond, with quotation marks. You entered {arcSecond}.")
    list.sort()
    
    print(f"{len(list)} links")
    
    for x in list:
        print(x)
