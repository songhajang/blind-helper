# -*- coding: utf-8 -*-
import json, random, os
import speech_recognition as sr
from playsound import playsound
from bs4 import BeautifulSoup as bs

os.system('cls')

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
    from playsound import playsound
    from gtts import gTTS
    import os
    if _Text is None: 
        return "유효하지 않은 값 입니다."
    _Number = random.randint(1,99999)
    tts = gTTS(text = _Text, lang = 'ko')
    _FileName = f'./tts_data/{_Number}.mp3'
    try:
        tts.save(_FileName)
    except:
        return "에러가 발생 했습니다."
    cwd = os.getcwd()
    print(cwd)
    playsound('tts.mp3')
    if os.path.isfile(_FileName):
        os.remove(_FileName)

def main():
    # haley_tts("HelloWorld")

    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     audio = r.listen(source)
    #     spking_text = r.recognize_google(audio, language='ko')
    spking_text = '오늘 날씨가 좋네요'
    print('spking_text:', spking_text)

    zero_text = zero_fun('86a774cf-9074-48a3-ab51-6dd3e8649ed8', 11987300804, spking_text)
    one_text = one_fun('86a774cf-9074-48a3-ab51-6dd3e8649ed8', 11987300804, spking_text)
    print('zero_text:', zero_text)
    print('one_text', one_text)

    if spking_text in ["좋은거", '좋은걸', '맑은', '좋네요']:
        _haleyText = "네, 저도 오늘 날씨가 좋은거 같아요. 추울 수도 있으니 따뜻한 옷 챙겨입기 바래요!"
    elif spking_text in ['나빠요', "안좋은거", '안좋은', '안좋음', '안좋은걸']:
        _haleyText = "오늘 날씨는 안좋은거 같아요. 오늘은 우산 같은걸 챙겨 보는건 어떨까요?"
    else:
        _haleyText = "오늘의 날씨가 어때라고 한번 말해보세요!"

    print(f"""
<<<<<<<<<< "{spking_text}" >>>>>>>>>>

감성 분석 지수 : {round(zero_text['score'] * 100, 2)}
현재 감성 : {zero_text['label']}

────────────────────────────────────

감정 분석 지수 : {round(one_text['Result'][0][0] * 100, 2)}
현재 감정 : {one_text['Result'][0][1]}

답변 내용 : {_haleyText}
""")

    haley_tts(_haleyText)

    # if zero_text['score'] < 0.98:
    #     print(zero_text['label'])
    # elif one_text['Result'][0][0] < 0.98:
    #     print(one_text['Result'][0][1])
    # else:
    #     print('홀리몰리')

main()