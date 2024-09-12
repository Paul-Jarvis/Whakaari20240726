#Script to get, in pixels, the height of the volcanic plume from the Te Kaha camera

## Import python packages
import cv2

## Input parameters ############################################################

#Video file name
vidFile = '/scratch/paulj/Whakaari/20240726/tekaha_20240725T1816-1920.mp4'

#Interval between frames (s)
int = 1

#Output file for night time lens
outFile = '/scratch/paulj/Whakaari/20240726/tekahaNightHeight.csv'

#Output file for day time lens
outFile = '/scratch/paulj/Whakaari/20240726/tekahaDayHeight.csv'

#Smallest number of frames at which plume might possibly appear
minFrames = 1200

## Read in video ###############################################################
vObj = cv2.VideoCapture(vidFile)

## Determine frame in which plume first appears ################################
for i in range(minFrames):
    ret, frame = vObj.read()

i = 1
while (vObj.isOpened()):
    ret, frame = vObj.read();
    #cv2.imshow('Frame', frame)
    #key = cv2.waitKey(0)
    frameFile = '/scratch/paulj/Whakaari/20240726Frames/' + str(i) + '.png'
    cv2.imwrite(frameFile, frame)
    i = i + 1
    """
    pause(0.00001);
    frame_h = get(handle(gcf),'JavaFrame');
    set(frame_h,'Maximized',1);
    query = input('Has plume appeared? y/n', 's');

    if isequal(query, 'y')
        disp('Click on plume top')
        [xPos(1), yPos(1)] = ginput(1);
        time(1) = 0;

        startTime = ...
            input('Please enter timestamp shown in format YYYYMMDDTHHMM', ...
            's')
        break
    end

end
"""
