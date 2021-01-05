
from core import DT
from core import detect_video
import argparse

parser = argparse.ArgumentParser(description='Faint Detection')
parser.add_argument("--video_path", dest = 'video_path', help = 
                    "Video to run detection upon",
                    default = "video.avi", type = str)
parser.add_argument("--model_path", dest = "model_path", help = "The model", default = "data/faint.h5", type = str)
parser.add_argument("--score", dest = "score", help = "Object Confidence to filter predictions", default = 0.5, type = float)
parser.add_argument("--classes_path", dest = "classes_path", help = "Class path", default = "data/name.txt", type = str)
parser.add_argument("--anchors_path", dest = 'anchors_path', help = 
                    "Anchor file",
                    default = "data/anchors.txt", type = str)
parser.add_argument("--font_path", dest = 'font_path', help = 
                    "Font file",
                    default = "font/FiraMono-Medium.otf", type = str)
args = parser.parse_args()
if __name__ == '__main__':
    #video_path='path2your-video'
    #video_path='E:\\FFOutput\\视频合并190325191159~1.mp4'
    detect_video(DT(), args.video_path)
