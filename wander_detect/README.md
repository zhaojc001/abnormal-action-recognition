test
video：
python video.py --video_path video_demo/wander1.avi  --model_path data/wander.h5  --anchors_path data/anchors.txt  --classes_path data/classes.txt --font_path font/FiraMono-Medium.otf --score 0.3
webcam：
python webcam.py --set_camera 0 --model_path data/wander.h5  --anchors_path data/anchors.txt  --classes_path data/classes.txt --font_path font/FiraMono-Medium.otf --score 0.3

参数说明：
    --video_path ：输入视频路径
    --set_camera ：免驱摄像头编号，默认0
    --model_path ：模型路径
    --anchors_path：先验框路径
    --classes_path ：类别文件路径
    --font_path ：设置字体路径
    --score ：置信度


