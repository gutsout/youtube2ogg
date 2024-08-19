# youtube2ogg 📹

Quick YouTube video to Ogg Vorbis Converter. Instead of downloading YouTube videos from sketchy websites, using Audacity to convert and compress `.mp3` to `.ogg` - provide a YouTube link to script and receive compressed to 22kHz `.ogg` file that is ready to go inside your mission file.

## How to Configure 🧰
### 1. Clone this Repository 
```
git clone https://github.com/gutsout/youtube2ogg.git
```

### 2. Install Python3

Ensure you have Python3 installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

[How to Install Python3 on Windows 10](https://www.digitalocean.com/community/tutorials/install-python-windows-10)

### 3. Install FFmpeg Executable:
You need to install the actual ffmpeg executable, which **yt-dlp** uses to process audio files.

**On Windows:** 

[FFmpeg Installation Guide](https://phoenixnap.com/kb/ffmpeg-windows)

**OR** download FFmpeg and copy contents of `bin/` directory to the script directory.

**On Linux:**
* Use your package manager to install ffmpeg:
```
sudo apt-get install ffmpeg
```

### 4. Install Python Dependencies:
Navigate to the project directory and install the required Python packages:
```
pip install -r requirements.txt
```
  
## Usage 
Find a YouTube video that you want to convert to `.ogg`. Copy a URL and use it with a script:
```
python3 youtube2ogg.py "https://www.youtube.com/watch?v=example"
```

## Future Plans 🏃
* Add parameter to change sample rate (lower sample rate -> worse audio quality -> less size). Currently sample rate is hardcoded to 22kHz.
* Display input and output files sizes.
