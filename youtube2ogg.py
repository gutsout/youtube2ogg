import yt_dlp
import sys
import os
from pydub import AudioSegment
from progress.spinner import PixelSpinner
from time import sleep

# Check if the URL was provided as a command-line argument
if len(sys.argv) > 1 and sys.argv[1] != '':
    url = str(sys.argv[1])
else:
    print("""[i] Usage: python3 yt2mp3.py URL        
[i] Example: python3 yt2mp3.py https://www.youtube.com/watch?v=example""")
    exit(1)

def download_youtube_mp3(url, output_path='./'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            output_filename = ydl.prepare_filename(info_dict)
            output_filename = output_filename.rsplit('.', 1)[0] + ".mp3"
        print(f"Download and conversion complete! Output file: {output_filename}")
        return output_filename
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
        return None

# Credit to Klairm (https://github.com/Klairm)
def converter(mp3_filename, target_sample_rate=22000):
    if mp3_filename and os.path.exists(mp3_filename):
        name = os.path.splitext(mp3_filename)[0]
        with PixelSpinner(f'[.mp3 -> .ogg] {name} Processing... ') as bar:
            for i in range(100):
                sleep(0.03)
                bar.next()


            sound = AudioSegment.from_mp3(mp3_filename)
            sound = sound.set_frame_rate(target_sample_rate)
            ogg_filename = f"{name}.ogg"
            sound.export(ogg_filename, format="ogg")
            print(f"\nConversion complete! Output file: {ogg_filename}")
            return ogg_filename
    else:
        print("MP3 file not found for conversion.")
        return None


output_file = download_youtube_mp3(url)
if output_file:
    converter(output_file)
