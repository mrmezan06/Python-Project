import ffmpeg
import argparse
import os

# Split a video file by given time period


def split_video(input_file, start_time, end_time, output_file):
    (
        ffmpeg
        .input(input_file, ss=start_time, to=end_time)
        .output(output_file)
        .run()
    )


if __name__ == "__main__":
    input_file = "C:/Users/Mejanur/Desktop/PyGame/Split a video file by given time period/s6e1.mp4"
    start_time = 0
    end_time = 50
    output_file = "out1.mp4"
    split_video(input_file, start_time, end_time, output_file)
    print("Done")

# Usage
# python videosplitter.py test.mp4 0 50 out1.mp4 out2.mp4
# python videosplitter.py -h
