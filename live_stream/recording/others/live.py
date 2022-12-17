# good doc for ffmpeg_streaming, js, hls, dash
# https://video.aminyazdanpanah.com/python/start?r=hls
# https://github.com/Dash-Industry-Forum/dash.js
# https://github.com/video-dev/hls.js


from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import ffmpeg_streaming


# 3. Stream(DASH or HLS) To File:
video = ffmpeg_streaming.input('http://192.168.0.105:8080/hls/test.m3u8')
# video = ffmpeg_streaming.input('rtmp://192.168.0.105:1935/live/test')
stream = video.stream2file(Formats.h264())

print("Recording...")
stream.output('./new-video.mp4')


# pip install ffmpeg-python
# https://json2video.com/how-to/ffmpeg-course/ffmpeg-wrappers.html#python
import ffmpeg
stream = ffmpeg.input('rtmp://192.168.0.105:1935/live/test')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4', **{'c': 'copy', 'f': 'mp4'})
ffmpeg.run(stream)


# # 1. HLS To DASH
# video = ffmpeg_streaming.input('https://www.aminyazdanpanah.com/?PATH/TO/HLS-MANIFEST.M3U8')
# _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
# dash = video.dash(Formats.h264())
# dash.representations(_480p)
# dash.output('/var/media/dash.mpd')



# #2. DASH To HLS
# video = ffmpeg_streaming.input('https://www.aminyazdanpanah.com/?PATH/TO/DASH-MANIFEST.MPD')
# hls = video.hls(Formats.h264())
# hls.auto_generate_representations()
# hls.output('/var/media/hls.m3u8')

