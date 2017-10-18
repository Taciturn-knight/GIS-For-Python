''' This module is Vector Layers operation fun '''
import os
import sys
# Is Ogr Installed
try:
    from osgeo import ogr
except:
    sys.exit('ERROR: cannot find GDAL/OGR modules')

def delete_file(driver_name, file_name):
    ''' delete a geo file '''
    driver = ogr.GetDriverByName(driver_name)
    if os.path.exists(file_name):
        driver.DeleteDataSource(file_name)

def ogr_drivers():
    ''' This coude returns the list of OGR drivers alphabetically from A-Z '''
    cnt = ogr.GetDriverCount()
    formats_list = []

    for i in range(cnt):
        driver = ogr.GetDriver(i)
        driver_name = driver.GetName()
        if not driver_name in formats_list:
            formats_list.append(driver_name)

    formats_list.sort()

    for i in formats_list:
        print i
    print "The number of ogr drivers is %d" % (cnt)

def is_driver_available(driver_name):
    ''' This fun check 'driver_name' driver is available. '''
    if ogr.GetDriverByName(driver_name) is None:
        print '%s driver not available. \n' % driver_name
        return False
    else:
        print '%s driver is available. \n' % driver_name
        return True

def ogr_driver_available_by_name():
    ''' This fun shows "ESRI Shapefile", "PostgreSQL", "FileGDB" and "SDE" OGR driver is available. '''

    # Shapefile available?
    is_driver_available("ESRI Shapefile")

    # PostgreSQL available?
    is_driver_available("PostgreSQL")

    # Is File GeoDatabase available?
    is_driver_available("FileGDB")

    # SDE available?
    is_driver_available("SDE")

if __name__ == '__main__':
#    delete_file("ESRI Shapefile", r'd:\GIS data source\lines.shp')
#    ogr_drivers()
    ogr_driver_available_by_name()
