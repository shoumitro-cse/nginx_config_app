
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

docker run -d -p 1935:1935 -p 8080:8080 alqutami/rtmp-hls

For Alpine-based Image use:
docker run -d -p 1935:1935 -p 8080:8080 alqutami/rtmp-hls:latest-alpine

To run with custom conf file:
docker run -d -p 1935:1935 -p 8080:8080 -v custom.conf:/etc/nginx/nginx.conf alqutami/rtmp-hls

rtmp://<server ip>:1935/live/<stream_key>. where <stream_key> is any stream key you specify.

example:

# for OBS Studio 
url: rtmp://192.168.0.105:1935/live
stream key: abc123

# for vlc
network stream url: rtmp://192.168.0.105:1935/live/abc123


Another example:
http://192.168.0.105:8080/stats
http://192.168.0.105:8080/players/rtmp.html
http://192.168.0.105:8080/players/hls.html
rtmp://192.168.0.105:1935/live/abc123


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
