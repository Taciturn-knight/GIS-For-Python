''' This module is Taxi Path homework '''
import sys 
import os

# Is GDAL/OGR Installed
try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERROR: cannot find GDAL/OGR modules')

# Enable python Exections

gdal.UseExceptions()

# Install GDAL/OGR error handler

def gdal_error_hander(err_class, err_num, err_msg):
    ''' This fun is used to show more clearly error info'''
    err_type = {
        gdal.CE_None: 'None',
        gdal.CE_Debug: 'Debug',
        gdal.CE_Warning: 'Warning',
        gdal.CE_Failure: 'Failure',
        gdal.CE_Fatal: 'Fatal'
    }

    err_msg = err_msg.replace('\n', ' ')
    err_class = err_type.get(err_class, 'None')
    print 'Error Number : %s' % (err_num)
    print 'Error Type:    %s' % (err_class)
    print 'Error Message: %s' % (err_msg)

if __name__ == '__main__':
    # install error handler
    gdal.PushErrorHandler(gdal_error_hander)

    gdal.Error(1, 2, 'test error')

    # for support chinese character in file path
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")

    # for support chinese character in attribute table field
    gdal.SetConfigOption("SHAPE_ENCODING", "")

    # register all drivers