from random import randint

from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
num = randint(100000,999999)
data = audio.generate(str(num))
audio.write(str(num), str(num)+'.mp3')
print(num)