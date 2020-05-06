import os
import subprocess as s

from gtts import gTTS
from pydub import AudioSegment


def tts(texto, save="./teste.mp3", slow=False, lang="pt-br"):  # ok
    voice = gTTS(text=texto, lang=lang, slow=slow)
    voice.save(save)


def tts_array(textos=[], output="./output.mp3", tmp="./tmp.mp3", delay_virgula=200, delay_ponto=500, lang="pt-br",
              slow=False):  # ok
    tts(textos[0], save=tmp, lang=lang, slow=slow)
    audio = AudioSegment.from_mp3(tmp)
    textos.remove(textos[0])
    for texto in textos[0:]:
        if texto == ",":
            audio += AudioSegment.silent(duration=delay_virgula)
        elif texto == ".":
            audio += AudioSegment.silent(duration=delay_ponto)
        else:
            tts(texto, save=tmp, lang=lang, slow=slow)
            audio += AudioSegment.from_mp3(tmp)
    os.remove(tmp)
    audio.export(output)


def tts_string(texto, output="./output.mp3", tmp="./tmp.mp3", delay_virgula=200, delay_ponto=500, lang="pt-br",
               slow=False):  # ok
    tmp1 = 0
    audio = AudioSegment.silent(duration=0)
    for i in range(0, len(texto)):
        print(texto[tmp1:i])
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


tts_string(
    "esse é um teste da nova função,se tudo estiver funcionando corretamente,haverão duas pequenas pausas.seguidas por uma longa pausa",
    output="teste.mp3")
s.call(["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", './teste.mp3'])
