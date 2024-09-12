#Script to get, in pixels, the height of the volcanic plume from the Te Kaha camera

## Import python packages
import cv2
import sys
from scipy.interpolate import interp1d
import numpy as np

sys.path.insert(1, '/home/paulj/Documents/windCalib/pythonVersion')

from extractWeather_function import extract_weather

## Input parameters ############################################################

#Video file name
vidFile = '/scratch/paulj/Whakaari/20240726/tekaha_20240725T1816-1920.mp4'
# vidFile = '/home/paulj/Documents/VMG/Whakaari/videos/tekaha_20240725T1816-1920.mp4'

#Interval between frames (s)
int = 1

#Output file for night time lens
outFile = '/scratch/paulj/Whakaari/20240726/tekahaNightHeight.csv'

#Output file for day time lens
outFile = '/scratch/paulj/Whakaari/20240726/tekahaDayHeight.csv'

#Smallest number of frames at which plume might possibly appear
minFrames = 1

#Time of first frame (YYYY-MM-DD HH:MM)
firstTime = '2024-07-25 18:16:00'

#File path to met data
metFile = '/scratch/paulj/Whakaari/20240726/era5_pl.nc'

#Vent location (to nearest 1/4 of a degree)
ventLat = -37.5
ventLong = 177.25

#Height (in m a.s.l) over which to calculate wind orientation (check back against
#this)
topPoint_Wind = 3000.0

#Vent altitude
vent_z = 0.0

## Read in weather data ########################################################
netCDF = extract_weather(metFile, firstTime, metFile, ventLat, ventLong)

## Add zero wind at sea level
netCDF.z = np.append(netCDF.z, 0.0)
netCDF.u = np.append(netCDF.u, 0.0)
netCDF.v = np.append(netCDF.v, 0.0)

## Get orientation  of the wind above the volcano #############################
wind_v_interp_f = interp1d(netCDF.z, netCDF.v) #Determine the wind velocity (v
                                              #component) of the range defined at
                                              #the base by the height of the vent
                                              #and at the top by the
                                              #topPoint_wind
wind_u_interp_f = interp1d(netCDF.z, netCDF.u) #Determine the wind velocity (u
                                              #component) of the range defined at
                                              #the base by the height of the vent
                                              #and at the top by the
                                              #topPoint_wind

nHeights = np.rint(topPoint_Wind - vent_z).astype(np.int32) + 1

z_array = np.linspace(vent_z, topPoint_Wind, nHeights)

wind_v = wind_v_interp_f(z_array)

wind_u = wind_u_interp_f(z_array)

ori = np.arctan2(wind_v, wind_u) #Calulate the wind oriention of the height
                                 #range of interest
ori = np.degrees(ori)

"""
## Read in video ###############################################################
vObj = cv2.VideoCapture(vidFile)

## Determine frame in which plume first appears ################################
#for i in range(minFrames):
#ret, frame = vObj.read()
#cv2.imshow('Frame', frame)
#key = cv2.waitKey(0)
while (vObj.isOpened()):
    ret, frame = vObj.read();
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(0)
    #pause(0.00001);
    #frame_h = get(handle(gcf),'JavaFrame');
    #set(frame_h,'Maximized',1);
    #query = input('Has plume appeared? y/n', 's');

    #if isequal(query, 'y'):
    #    disp('Click on plume top')
    #    [xPos(1), yPos(1)] = ginput(1);
    #    time(1) = 0;

    #    startTime = ...
    #        input('Please enter timestamp shown in format YYYYMMDDTHHMM', ...
    #        's')
    #    break
    #end

end
"""
