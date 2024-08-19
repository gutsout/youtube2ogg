# youtube2ogg

Quick YouTube to Ogg Vorbis Converter. Provide a YouTube link and receive compressed to 22kHz `.ogg` file that's ready to go inside your mission file.
## How to Use

1. Clone this Repository
```
git clone https://github.com/gutsout/youtube2ogg.git
cd youtube2ogg
```

2. Install Python3

Ensure you have Python 3 installed on your system. You can download it from python.org.
[How to Install Python](https://www.digitalocean.com/community/tutorials/install-python-windows-10)

4. Install FFmpeg Executable:
You need to install the actual ffmpeg executable, which yt-dlp uses to process audio files.

**On Windows:**

[FFmpeg Installation Guide](https://phoenixnap.com/kb/ffmpeg-windows)
    
**On macOS:**
* Use Homebrew to install ffmpeg:
```
brew install ffmpeg
```

**On Linux:**
* Use your package manager to install ffmpeg:
```
sudo apt-get install ffmpeg
```

4. Install Python Dependencies:
Navigate to the project directory and install the required Python packages:
```
# Install requirements
pip install -r requirements.txt
```
  
# Usage
```
python3 youtube2ogg.py "https://www.youtube.com/watch?v=example"
```
