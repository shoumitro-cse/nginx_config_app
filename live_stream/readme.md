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

docker-compose -f docker-compose.yml up --build
example:

# for OBS Studio 
url: rtmp://192.168.0.105:1935/live

# for vlc
network stream url: rtmp://192.168.0.105:1935/live

```

### Docker image for video streaming server that supports RTMP, HLS, and DASH streams.
```
docker-compose -f docker-compose2.yml up --build

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

# for vlc
network stream url: rtmp://192.168.0.105:1935/live/abc123


# Another example:

# live stream status
http://192.168.0.105:8080/stats  
http://192.168.0.105:8080/stat.xsl

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
