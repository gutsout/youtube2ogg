# youtube2ogg

Quick YouTube to Ogg Vorbis Converter. Provide a YouTube link and receive compressed to 16kHZ `.ogg` file that's ready to go inside your mission file.
## How to Use

1. Clone this Repository
```
git clone https://github.com/yourusername/youtube2ogg.git
cd youtube2ogg
```

2. Install Python3
Ensure you have Python 3 installed on your system. You can download it from python.org.

3. Install FFmpeg Executable:
You need to install the actual ffmpeg executable, which yt-dlp uses to process audio files.
**On Windows:**
* Download the latest static build of FFmpeg from the official FFmpeg website.
* Extract the contents and place the `bin` folder somewhere on your system (e.g., `C:\ffmpeg\bin`).
* Add the path to the bin folder to your system's **PATH** environment variable.

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