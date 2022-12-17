rtmp_url = "rtmp://192.168.0.105:1935/live/test"

import subprocess as sp
import cv2

#rtmpUrl = "rtmp://a.rtmp.youtube.com/live2/key"
#rtmp_url = "rtmp://127.0.0.1:1935/live/test"  # Use localhost for testing
camera_path = "BigBuckBunny.mp4"
cap = cv2.VideoCapture(camera_path)

# Get video information
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Start the TCP server first, before the sending client (for testing).
ffplay_process = sp.Popen(['ffplay', '-listen', '1', '-i', rtmp_url])  # Use FFplay sub-process for receiving the RTMP video.

# ffmpeg command
# OpenCV does not support audio.
command = ['ffmpeg',
        '-y',
        '-re', # '-re' is requiered when streaming in "real-time"
        '-f', 'rawvideo',
        #'-thread_queue_size', '1024',  # May help https://stackoverflow.com/questions/61723571/correct-usage-of-thread-queue-size-in-ffmpeg
        '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', "{}x{}".format(width, height),
        '-r', str(fps),
        '-i', '-',
        '-vn', '-i', camera_path,  # Get the audio stream without using OpenCV
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        # '-c:a', 'aac',  # Select audio codec
        '-bufsize', '64M',  # Buffering is probably required
        '-f', 'flv', 
        rtmp_url]

command = ['ffmpeg', '-y',
        '-i', rtmp_url,
        # '-async', '1', 
        # '-vsync', '-1',
        # '-tune', 'zerolatency',
        # '-preset', 'superfast',
        # '-crf', '23',
        '-c', 'copy',
        '-f', 'mp4', 
        'my_output_file.mp4']
# Pipeline configuration
p = sp.Popen(command, stdin=sp.PIPE)

# read webcamera
while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        print("End of input file")
        break

    # write to pipe
    p.stdin.write(frame.tobytes())

p.stdin.close()  # Close stdin pipe
p.wait()

ffplay_process.kill()  # Forcefully close FFplay sub-process
