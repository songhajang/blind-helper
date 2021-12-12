# -*- coding: utf-8 -*-
import json, random, os
import speech_recognition as sr
from bs4 import BeautifulSoup as bs

def zero_fun(key: str, ser_id: int, _Text: str):
    import requests
    if _Text is None: return "지원하지 않는 형식 입니다."
    datas = {
        "key": key,
        "serviceId": ser_id,
        "argument": {
            "type": "0",
            "query": _Text
        }
    }
    url = 'http://svc.saltlux.ai:31781'

    headers = {'Content-Type':'application/json;'}
    requests = requests.post(url, headers = headers, json = datas)
    if requests.status_code == 200:
        zero_Text = json.loads(requests.text)
        return zero_Text

def one_fun(key: str, ser_id: int, _Text: str = None):
    import requests
    if _Text is None: return "지원하지 않는 형식 입니다."
    datas = {
        "key": key,
        "serviceId": ser_id,
        "argument": {
            "type": "1",
            "query": _Text
        }
    }
    url = 'http://svc.saltlux.ai:31781'

    headers = {'Content-Type':'application/json;'}
    requests = requests.post(url, headers=headers, json = datas)
    if requests.status_code == 200:
        one_Text = json.loads(requests.text)
        return one_Text

def haley_tts(_Text: str = None):
    import playsound
    from gtts import gTTS
    if _Text is None: return "유효하지 않은 값 입니다."
    _Number = random.randint(1,99999)
    tts = gTTS(text = _Text, lang = 'ko')
    _FileName = f'./tts_data/{_Text}_{_Number}.mp3'
    try:
        tts.save(_FileName)
    except:
        return "에러가 발생 했습니다."
    playsound.playsound(_FileName)
    if os.path.isfile(_FileName):
        os.remove(_FileName)

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    spking_text = r.recognize_google(audio, language='ko')

zero_text = zero_fun('86a774cf-9074-48a3-ab51-6dd3e8649ed8', 11987300804, spking_text)
one_text = one_fun('86a774cf-9074-48a3-ab51-6dd3e8649ed8', 11987300804, spking_text)
print(zero_text)
print(one_text)
# haley_tts('테스트')

# if zero_text['score'] < 98 or one_text['Result'][0][0] < 98:
#     print(1)