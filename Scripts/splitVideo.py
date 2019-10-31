import subprocess
import re
import math
import argparse
import shlex


length_regexp = 'Duration: (\d{2}):(\d{2}):(\d{2})\.\d+,'
re_length = re.compile(length_regexp)

def splitVideo(pathIn):
    ffmpeg = subprocess.Popen(["ffmpeg", "-i", pathIn], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output = subprocess.Popen(["grep", 'Duration'], stdin=ffmpeg.stderr, stdout=subprocess.PIPE, universal_newlines=True).stdout.read()
    
    matches = re_length.search(output)
    if matches:
        video_length = int(matches.group(1)) * 3600 + \
                        int(matches.group(2)) * 60 + \
                        int(matches.group(3))
        print("Video length in seconds: " + str(video_length))

	one_percent = video_length/100.0   
    video_partials = {
            "vocabulario1": {
                    "start": 0,
                    "end":  math.ceil(one_percent*6),
                    },
            "vocabulario2": {
                    "start": math.ceil(one_percent*4.5),
                    "end":  math.ceil(one_percent*10.5),
                    },
            "vocabulario3": {
                    "start": math.ceil(one_percent*9),
                    "end":  math.ceil(one_percent*15),
                    },
            "teste": {
                    "start": math.ceil(one_percent*15)+1,
                    "end":  video_length,
                    },
            }
    

    for key, value in video_partials.items():
        split_cmd = "ffmpeg -i '" +pathIn + "' -vcodec copy "

        split_str = " -ss " + str(value["start"])+ " -to " + str(value["end"]) + \
                    "  -an '"+pathIn[:-4] + "-" + key + "." + pathIn[-3:] + \
                    "'"
        print("About to run: " + split_cmd + split_str)
        subprocess.check_call(shlex.split(split_cmd + split_str), universal_newlines=True)


if __name__ == '__main__':
    argument = argparse.ArgumentParser()

    argument.add_argument(
            "--pathIn", "-i",
            help="path to video",
            )
    
    args = argument.parse_args()
    print(args)
    
    splitVideo(args.pathIn)
