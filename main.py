from scripts.extract_audio import extract_audio
from scripts.speech_to_text import transcribe_audio
from scripts.translate import translate_text
from scripts.text_to_speech import synthesize_speech
# from scripts.synchronize_lip import synchronize_lip
# from scripts.merge_audio_video import merge_audio_video

import os
from dotenv import load_dotenv


def main(video_path):
    # extract audio
    extract_audio('data/input/sample.mp4',
                  'data/extracted_audio/sample.wav')

    # audio to text
    transcript = transcribe_audio('data/extracted_audio/sample.wav', creds)
    with open('data/translated_text/sample_en.txt', 'w') as f:
        f.write(transcript)

    # translate english text to hindi
    with open('data/translated_text/sample_en.txt', 'r') as f:
        english_text = f.read()

    translated_text = translate_text(english_text, creds)
    with open('data/translated_text/sample_hi.txt', 'w') as f:
        f.write(translated_text)

    # Hindi text to audio
    with open('data/translated_text/sample_hi.txt', 'r') as f:
        hindi_text = f.read()

    synthesize_speech(hindi_text, 'data/generated_audio/sample_hi.wav',creds)


if __name__ == '__main__':

    load_dotenv()
    creds = os.getenv('GCP_CREDS_PATH')
    main('data/input_video/sample.mp4')
