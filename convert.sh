#!/bin/bash

# Bash script to convert .mxg files to .mp4

#inFile='/scratch/paulj/Whakaari/20240726/netcam-tekaha_20240725T1616-1715.mxg'
#outFile='/scratch/paulj/Whakaari/20240726/tekaha_20240725T1616-1715.mp4'

#ffmpeg -i $inFile -f mp4 -vcodec libx264 -vsync 2 -max_muxing_queue_size 9999 $outFile
ffmpeg -i $1 -f mp4 -vcodec libx264 -vsync 2 -max_muxing_queue_size 9999 $2
