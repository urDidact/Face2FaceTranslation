from google.cloud import speech
from google.oauth2 import service_account


def transcribe_audio(audio_file_path,creds):

    credentials = service_account.Credentials.from_service_account_file(creds)
    client = speech.SpeechClient(credentials=credentials)


    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "

    return transcript

