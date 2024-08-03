from google.cloud import translate_v2 as translate
from google.oauth2 import service_account




def translate_text(text,creds, target_language='hi'):
    credentials = service_account.Credentials.from_service_account_file(creds)
    translate_client = translate.Client(credentials=credentials)

    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']



