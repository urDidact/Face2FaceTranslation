from google.cloud import texttospeech
from google.oauth2 import service_account

def synthesize_speech(text, output_audio_path,creds):
    credentials = service_account.Credentials.from_service_account_file(creds)
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="hi-IN",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_audio_path, 'wb') as out:
        out.write(response.audio_content)

