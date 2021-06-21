## Raspberry Pi automated video player
With the Raspberry Pi connected to an HDMI television or projector, a USB key holding mutiple video files is plugged in. The video files found on the device will be played sequentially in repeat loop.<br/>
<br/>
A headless image can be used for this setup as no Graphic User Interface is required. Prepare your SD card with Raspberry Lite OS. SD card can be a minimum size of 4Gb in this case.<br/>
<br/>
The USB key used to introduce the video files must be formatted FAT16 or FAT32. The files must be prepared in MP4 format. Naming of the files are best managed if prepared numerically according to the order we wish to play the videos one after the other (ex: 001.mp4, 002.mp4, 003.mp4...) <br/>

Dependencies are as follows:

```bash
sudo apt-get update
sudo apt-get install python3-pygame
```

Python3 is used to execute the included code _videoPlayer.py_ . As follows: <br/>

```bash
python3 /path/to/file/videoplayer.py
```

After verification of no errors at execution of the file, insert this command at the end of the .bashrc file found in the user home folder. The command will then launch at startup. In order to complete the setup, be sure to choose console auto-login in preferences (no GUI required):

```bash
sudo raspi-config
```

A Dev folder is included in this repository (named VideoPlayerDev). The files found here are the building blocks used to create the code. It is included here "as-is". Little commentary is provided, but should be self-explanatory for a seasoned python programmer.
