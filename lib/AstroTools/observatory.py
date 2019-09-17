# module with tools to calculate properties of a given observatory setup

import astropy.units as u
import math as m

# this function calculated angular field of view at the camera
# param: - focal_len : telescope's focal length, mm
#        - sensor_d  : single dimension of the sensor, mm
# returns: angular field of view, arcseconds
def calc_FOV(focal_len, sensor_d):
    a = 2 * m.degrees(m.atan(sensor_d/(2 * focal_len))) * u.deg    # gets angular fov in degrees
    return a.to(u.arcsec).value