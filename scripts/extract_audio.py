import os
import subprocess


def extract_audio(video_path, audio_output_path, bitrate='312k'):
    command = [
        'ffmpeg',
        '-i', video_path,       
        '-vn',                  
        '-acodec', 'pcm_s16le', 
        '-ar', '16000',         
        '-ac', '1',             
        '-b:a', bitrate,        
        audio_output_path      
    ]
    subprocess.run(command, check=True)

#
# extract_audio('data/input/sample.mp4', 'data/extracted_audio/sample.wav')
