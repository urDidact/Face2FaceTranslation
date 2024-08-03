import subprocess
import os

def synchronize_audio_video(video_path, audio_path, output_path, model_path='config/Wav2Lip/checkpoints/wav2lip_gan.pth'):
 
    inference_script = 'config/Wav2Lip/inference.py'
   
    command = [
        'python', inference_script,
        '--checkpoint_path', model_path,
        '--face', video_path,
        '--audio', audio_path,
        '--outfile', output_path,
    ]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


video_file = 'data/input/sample.mp4'
audio_file = 'data/generated_audio/sample_hi.wav'
output_file = 'data/final_video/final.mp4'

# synchronize_audio_video(video_file, audio_file, output_file)