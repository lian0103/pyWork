from gtts import gTTS
import pygame

# 初始化pygame
pygame.init()
pygame.mixer.init()

def text_to_speek(text):
    # 创建一个gTTS对象
    # tts = gTTS(text=text, lang='zh-TW')  # 语言代码可以根据需要更改
    tts = gTTS(text=text, lang='ja')
    tts.save("output.mp3")

    # 播放音频文件
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    # 等待音频播放完毕
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def close():
    # 退出pygame
    pygame.quit()




