### What is RTMP, HLS, DASH?
```
1. What is Stream RTMP (Real Time Messaging Protocol):
Ans: The Real-Time Messaging Protocol (RTMP) is a data transmission technology that 
supports live online video streaming. RTMP was initially designed to transport audio 
and video data between a dedicated streaming server and the Adobe Flash Player.

RTMP is a TCP-based protocol which maintains persistent connections and allows low-latency 
communication. To deliver streams smoothly and transmit as much information as possible, 
it splits streams into fragments, and their size is negotiated dynamically between the client and server.


2. What is Apple HTTP Live Streaming (HLS):
Ans: HTTP Live Streaming (HLS) sends audio and video over HTTP from an ordinary web server for 
playback on iOS-based devices—including iPhone, iPad, iPod touch, and Apple TV—and on desktop 
computers (macOS).

3. What is Dynamic Adaptive Streaming over HTTP (DASH) video formats:
Ans: Dynamic Adaptive Streaming over HTTP (DASH), also known as MPEG-DASH, is an adaptive 
bitrate streaming technique that enables high quality streaming of media content over the 
Internet delivered from conventional HTTP web servers.

DASH uses adaptive bitrate, allowing the video player to automatically adjust to network conditions 
and switch to lower or higher quality resolution. For example, when a user's bandwidth is low, 
streamed video will play at a lower quality level to use less bandwidth.


$ apt-get install nginx-plus-module-rtmp  

# nginx-plus-module-rtmp package used for
Stream video in multiple formats, including Real-Time Messaging Protocol (RTMP), HLS, and DASH, 
with the RTMP dynamic module, supported by NGINX, Inc.

```


### OBS Studio & nginx-rtmp live stram install
```
# install OBS Studio

https://obsproject.com/
sudo pacman -S flatpak
# flatpak install com.obsproject.Studio.flatpakref
flatpak install flathub com.obsproject.Studio
flatpak uninstall flathub com.obsproject.Studio
flatpak run com.obsproject.Studio


# install live stream
https://www.youtube.com/watch?v=EzmA8uksOG4
https://hub.docker.com/r/tiangolo/nginx-rtmp/

docker-compose -f docker-compose-rtmp.yml up --build
example:

# for OBS Studio 
url: rtmp://192.168.0.105:1935/live

# Terminal command for live video 
ffmpeg -re -i /home/shoumitro/Documents/FR/video_audio/image_video_processing/sample_vid.mp4 -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://192.168.0.105:1935/live

# vlc for to access live video 
network stream url: rtmp://192.168.0.105:1935/live

# live video recorder
ffmpeg -i "rtmp://192.168.0.105:1935/live" -c copy -f mp4 my_output_file.mp4

sudo ufw allow 1935/tcp

```

### Docker image for video streaming server that supports RTMP, HLS, and DASH streams.
```
docker-compose -f docker-compose-all.yml up --build

# docker images for live sreaming
https://hub.docker.com/r/alqutami/rtmp-hls

# simple
docker run -d -p 1935:1935 -p 8080:8080 alqutami/rtmp-hls

# For Alpine-based Image use:
docker run -d -p 1935:1935 -p 8080:8080 alqutami/rtmp-hls:latest-alpine

# To run with custom nginx conf file:
docker run -d -p 1935:1935 -p 8080:8080 -v custom_nginx.conf:/etc/nginx/nginx.conf alqutami/rtmp-hls

rtmp://<server ip>:1935/live/<stream_key>. where <stream_key> is any stream key you specify.

example:

# for OBS Studio 
url: rtmp://192.168.0.105:1935/live
stream key: abc123

# Terminal command for live video 

# Alternate of this url http://192.168.0.105:8080/players/rtmp.html
ffmpeg -re -i "/home/shoumitro/Documents/FR/video_audio/my_video.mp4" -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://192.168.0.105:1935/live/test

# for custom stream key
ffmpeg -re -i "/home/shoumitro/Documents/FR/video_audio/my_video.mp4" -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://192.168.0.105:1935/live/abc123

# vlc for to access live video 
network stream url: rtmp://192.168.0.105:1935/live/abc123

# live video recorder
ffmpeg -i "rtmp://192.168.0.105:1935/live/test" -c copy -f mp4 my_output_file.mp4
ffmpeg -i "http://192.168.0.105:8080/hls/test.m3u8" -c copy -f mp4 my_output_file.mp4

sudo ufw allow 1935/tcp
sudo ufw allow 8088/tcp

# add this line of code
docker exec -it live_stream_container bash
apt update
apt install nano

nano /usr/local/nginx/html/players/hls.html
<video id="player" class="video-js vjs-default-skin" width="720" controls preload="$
        <source src="/hls/abc123.m3u8" type="application/x-mpegURL" />
<!--         <source src="/hls/abc123_src.m3u8" type="application/x-mpegURL" />
        <source src="/hls/abc123_low.m3u8" type="application/x-mpegURL" />
        <source src="/hls/abc123_mid.m3u8" type="application/x-mpegURL" />
        <source src="/hls/abc123_high.m3u8" type="application/x-mpegURL" />
        <source src="/hls/abc123_hd720.m3u8" type="application/x-mpegURL" /> -->
</video>

nano /usr/local/nginx/html/players/dash.html
	<video id="player" class="video-js vjs-default-skin" width="720" controls preload="auto">
		<source src="/dash/test_src.mpd" type="application/dash+xml" />
<!-- 		<source src="/dash/test_low.mpd" type="application/dash+xml" />
		<source src="/dash/test_mid.mpd" type="application/dash+xml" />
		<source src="/dash/test_high.mpd" type="application/dash+xml" />
		<source src="/dash/test_hd720.mpd" type="application/dash+xml" /> -->
	</video>

# to see source video
ls /mnt/hls
ls /mnt/dash

# enter here to see live video
http://192.168.0.105:8080/players/hls.html
http://192.168.0.105:8080/players/dash.html


# Another example:

# live stream status
http://192.168.0.105:8080/stats  
http://192.168.0.105:8080/stat.xsl
# or inside docker container
cat /usr/local/nginx/html/stat.xsl 

# can't access these files
http://192.168.0.105:8080/hls  
http://192.168.0.105:8080/dash  

To play RTMP content (requires Flash): 
http://192.168.0.105:8080/players/rtmp.html

To play HLS content: 
http://192.168.0.105:8080/players/hls.html

To play HLS content using hls.js library: 
http://192.168.0.105:8080/players/hls_hlsjs.html

To play DASH content: 
http://192.168.0.105:8080/players/dash.html

To play RTMP and HLS contents on the same page: 
http://192.168.0.105:8080/players/rtmp_hls.html

```


### Library for python and js
```
# good doc for ffmpeg_streaming, js, hls, dash
# https://video.aminyazdanpanah.com/python/start?r=hls
# https://github.com/Dash-Industry-Forum/dash.js
# https://github.com/video-dev/hls.js
```


### RTMP live stream video recorder
```
# Recorder start
cd live_stream/
python recording/live_stream_recorder.py

output:
 pid: 7376

# to find pid
/proc/7376/

# Recorder cancle
python recording/live_stream_recorder_stop.py pid_here

example:
python recording/live_stream_recorder_stop.py 7376
``` 


### Recorder
```
docker exec -it live_stream_container bash
chown nobody /mnt
chmod 777 -R /mnt
mkdir -p /mnt/rec
# mkdir -p /mnt/hls
# mkdir -p /mnt/dash
chmod 777 -R /mnt/rec

# press this cmd to download record file to convert .mp4
ffmpeg -y -i http://192.168.0.105:8080/test.flv -acodec libmp3lame -ar 44100 -ac 1 -vcodec libx264 test.mp4
```