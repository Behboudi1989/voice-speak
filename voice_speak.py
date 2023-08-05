import time
import pyttsx3
import threading

voice_engine = pyttsx3.init()
voices = voice_engine.getProperty("voices")
voice_engine.setProperty("voice", voices[1].id)
voice_engine.setProperty("rate", 170)
voice_engine.setProperty("volume", 0.8)

def voice_speak(text):
    voice_engine.startLoop(False)
    voice_engine.say(text)
    voice_engine.iterate()
    voice_engine.endLoop()

def stop_early():
    time.sleep(voice_engine.getProperty("rate") * len(text_input) / 200.0 - 1)
    voice_engine.stop()

text_input = "Hello and welcome!"
text_input_2 = "We're happy that your're here"

threading.Thread(target=voice_speak, args=(text_input,)).start()
stop_early()