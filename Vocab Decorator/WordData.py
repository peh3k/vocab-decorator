from translate import Translator
from playsound import playsound
import os
from gtts import gTTS
import random

    

def get_audio(text, lang):
    tts = gTTS(text, lang=lang)
    tts.save("audio.mp3")


def play_and_remove_audio():
    playsound("audio.mp3")
    os.remove("audio.mp3")


def translate_to_portuguese(word):
    translator = Translator(to_lang="pt")
    translation = translator.translate(word)
    return translation


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            words = [word[:-1] for word in linhas[:-1]]
            words.append(linhas[-1])

            return words
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")


def word_classification():
    words = ler_arquivo("words.txt")
    easy_words = [word for word in words if len(word) < 4]
    median_words = [word for word in words if len(word) < 7 and len(word) > 5]
    hard_words = [word for word in words if len(word) > 7]

    return easy_words, median_words, hard_words

def choice_word(words):
    
    return random.choice(words).upper()


