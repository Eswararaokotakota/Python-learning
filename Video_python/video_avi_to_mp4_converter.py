import moviepy.editor as moviepy
import os


input_video = input("Enter .avi file path here: ")
video = moviepy.VideoFileClip(input_video)


video.write_videofile("video.mp4")