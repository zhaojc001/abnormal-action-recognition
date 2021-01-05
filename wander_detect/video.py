from core import *
import argparse
from core import DT
from core import detect_video
from core import main
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--video_path', default='video_demo/wander1.avi', type=str,
                    help='The input video path')
parser.add_argument("--model_path", dest = "model_path", help = "The model", default = "data/fight.h5", type = str)
parser.add_argument("--score", dest = "score", help = "Object Confidence to filter predictions", default = 0.3, type = float)
parser.add_argument("--classes_path", dest = "classes_path", help = "Class path", default = "data/name.txt", type = str)
parser.add_argument("--anchors_path", dest = 'anchors_path', help = 
                    "Anchor file",
                    default = "data/anchors.txt", type = str)
parser.add_argument("--font_path", dest = 'font_path', help = 
                    "Font file",
                    default = "font/FiraMono-Medium.otf", type = str)
args = parser.parse_args()
if __name__ == '__main__':
    main(DT(),args.video_path)
    

