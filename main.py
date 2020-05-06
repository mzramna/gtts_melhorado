import os
import subprocess as s

from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr

def tts(texto, save="./teste.mp3", slow=False, lang="pt-br"):  # ok
    voice = gTTS(text=texto, lang=lang, slow=slow)
    voice.save(save)


def tts_array(textos=[], output="./output.mp3", tmp="./tmp.mp3", delay=200, lang="pt-br",
              slow=False):  # ok
    tts(textos[0], save=tmp, lang=lang, slow=slow)
    audio = AudioSegment.from_mp3(tmp)
    textos.remove(textos[0])
    for texto in textos[0:]:
            audio += AudioSegment.silent(duration=delay)
            tts(texto, save=tmp, lang=lang, slow=slow)
            audio += AudioSegment.from_mp3(tmp)
    os.remove(tmp)
    audio.export(output)


def tts_string(texto, output="./output.mp3", tmp="./tmp.mp3", delay_virgula=200, delay_ponto=500, lang="pt-br",
               slow=False):  # ok
    tmp1 = 0
    audio = AudioSegment.silent(duration=0)
    for i in range(0, len(texto)):
        if texto[i] == ",":
            tts(texto[tmp1:i], save=tmp, lang=lang, slow=slow)
            audio += AudioSegment.from_mp3(tmp)
            os.remove(tmp)
            audio += AudioSegment.silent(duration=delay_virgula)
            tmp1 = i + 1

        elif texto[i] == ".":
            tts(texto[tmp1:i], save=tmp, lang=lang, slow=slow)
            audio += AudioSegment.from_mp3(tmp)
            os.remove(tmp)
            audio += AudioSegment.silent(duration=delay_ponto)
            tmp1 = i + 1
    tts(texto[tmp1:(len(texto))], save=tmp, lang=lang, slow=slow)
    audio += AudioSegment.from_mp3(tmp)
    os.remove(tmp)
    audio.export(output)

def stt(lang="pt-br"):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("diga algo")
        audio=r.listen(source)
        try:
            captado=r.recognize_google(audio,language=lang)
            return(captado)
        except Exception as e:
            print(e)
            return stt(lang)
# tts_string(
#     "esse é um teste da nova função,se tudo estiver funcionando corretamente,haverão duas pequenas pausas.seguidas por uma longa pausa",
#     output="teste.mp3")
capturado=stt()
print(capturado)
tts_string(capturado,output="teste_de_stt_to_tts.mp3")
s.call(["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", './teste_de_stt_to_tts.mp3'])