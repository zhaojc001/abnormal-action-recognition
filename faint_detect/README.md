test
video：
python video.py --video_path E:\input\1.mp4 --model_path data/faint.h5 --classes_path data/name.txt --anchors_path data/anchors.txt --font_path font/FiraMono-Medium.otf --score 0.991
webcam：
python webcam.py --set_camera 0 --model_path data/faint.h5 --classes_path data/name.txt --anchors_path data/anchors.txt --font_path font/FiraMono-Medium.otf --score 0.991

参数说明:
    --video_path 视频路径
    --set_camera 免驱摄像头编号
    --model_path 模型路径
    --classes_path 检测类别路径
    --anchors_path 默认框路径
    --score 置信度
    --font_path 窗口打印字体路径