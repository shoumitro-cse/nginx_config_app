# https://pypi.org/project/python-ffmpeg-video-streaming/
# https://stackoverflow.com/questions/70471732/pipe-and-opencv-to-ffmpeg-with-audio-streaming-rtmp-in-python


# best doc
# https://ffmpeg.org/pipermail/ffmpeg-user/2015-July/027642.html
# ffmpeg -i "rtmp://192.168.0.105:1935/live/test" -c copy -f mp4 my_output_file.mp4
# https://github.com/kkroening/ffmpeg-python/issues/162


rtmp_url = "rtmp://192.168.0.105:1935/live/test"
import subprocess as sp

command = ['ffmpeg', '-y',
        '-i', rtmp_url,
        '-c', 'copy',
        '-f', 'mp4', 
        'my_output_file.mp4']
sp.Popen(command)
#p = sp.Popen(command, stdin=sp.PIPE)






















# #import cv2  # Import OpenCV lib

# #cap = cv2.VideoCapture('rtmp://192.168.0.105:1935/live/test') # Open video source as object
# #while cap.isOpened():  # Untill end of file/error occured
# #    ret, frame = cap.read()  # Read frame as object - numpy.ndarray, ret is a confirmation of a successfull retrieval of the frame
# #    if ret: 
# #        print(ret)
# #        print(frame)
# #    else:
# #        break
# #cap.release()

# # ffmpeg -re -i "Introducing.mkv" -c:v copy -c:a aac -ar 44100 -ac 1 -f flv rtmp://192.168.0.105:1935/live/test

# import subprocess as sp
# import cv2

# # ffmpeg -i "rtmp://192.168.0.105:1935/live/test" -c copy -f mp4 test.mp4

# #rtmpUrl = "rtmp://a.rtmp.youtube.com/live2/key"
# rtmp_url = "rtmp://192.168.0.105:1935/live/test"  # Use localhost for testing
# camera_path = "BigBuckBunny.mp4"
# cap = cv2.VideoCapture(camera_path)

# # Get video information
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Start the TCP server first, before the sending client (for testing).
# ffplay_process = sp.Popen(['ffplay', '-listen', '1', '-i', rtmp_url])  # Use FFplay sub-process for receiving the RTMP video.

# # ffmpeg command
# # OpenCV does not support audio.
# command = ['ffmpeg',
#         '-y',
#         '-re', # '-re' is requiered when streaming in "real-time"
#         '-f', 'rawvideo',
#         '-thread_queue_size', '1024',  # May help https://stackoverflow.com/questions/61723571/correct-usage-of-thread-queue-size-in-ffmpeg
#         '-vcodec','rawvideo',
#         '-pix_fmt', 'bgr24',
#         '-s', "{}x{}".format(width, height),
#         '-r', str(fps),
#         '-i', '-',
#         '-vn', '-i', camera_path,  # Get the audio stream without using OpenCV
#         '-c:v', 'libx264',
#         '-pix_fmt', 'yuv420p',
#         '-preset', 'ultrafast',
#          '-c:a', 'aac',  # Select audio codec
#         '-bufsize', '64M',  # Buffering is probably required
#         '-f', 'flv', 
#         rtmp_url]


# print(command)

# # Pipeline configuration
# p = sp.Popen(command, stdin=sp.PIPE)
# print("\n\n")
# print(p)
# print("\n")

# # read webcamera
# while (cap.isOpened()):
#     ret, frame = cap.read()

#     print(ret, frame)
#     print("\n\n")

#     if not ret:
#         print("End of input file")
#         break

#     # write to pipe
#     p.stdin.write(frame.tobytes())

# p.stdin.close()  # Close stdin pipe
# p.wait()

# ffplay_process.kill()  # Forcefully close FFplay sub-process
