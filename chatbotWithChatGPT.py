import openai   # pip install openai
import json
import speech_recognition as sr
from gtts import gTTS
import os
import pygame


try:
    with open("chatGPT.txt", "r") as json_file:
        data = json.load(json_file)
        openai.api_key = data["openai_apikey"]
except FileNotFoundError:
    print(f"The file chatGPT.txt does not exist.")


def speak():
    r = sr.Recognizer()  # 預設辨識英文

    print(sr.Microphone.list_microphone_names())  # 列出所有的麥克風
    print("請說話，結束時，按下Ctrl+C  就可以辨識語音")
    # source = sr.Microphone(device_index=0)                       # 麥克風設定 0 內定
    microphone = sr.Microphone()  # 麥克風設定 0 內定
    with microphone as source:
        r.adjust_for_ambient_noise(source)  # 調整麥克風的雜訊
        audio = r.listen(source)  # 錄製的語音

    # str1 =r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", language="zh-TW")
    str1 = r.recognize_google(audio, language="zh-TW")  # 使用Google的服務
    print("辨識後的文字: " + str1)
    return str1


def getGPTAnswer(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "我會說中文"},
            {"role": "user", "content": text}
        ]
    )
    print(completion.choices[0].message)
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

# getGPTAnswer("hello")

def tts(text):
    # 创建一个gTTS对象
    tts = gTTS(text=text, lang='zh-TW')  # 语言代码可以根据需要更改

    # 保存语音文件
    tts.save("output.mp3")

    # 播放语音文件
    # os.system("mpg321 output.mp3")  # 使用mpg321播放mp3文件，您可以根据需要使用其他播放器


    # 初始化pygame
    pygame.init()

    # 创建一个音频对象
    pygame.mixer.init()

    # 播放音频文件
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    # 等待音频播放完毕
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # 退出pygame
    pygame.quit()

str = speak();
ans = getGPTAnswer(str)
tts(ans)
