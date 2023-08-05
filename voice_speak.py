import time
import pyttsx3
import threading

voice_engine = pyttsx3.init()
voices = voice_engine.getProperty("voices")
voice_engine.setProperty("voice", voices[1].id)
voice_engine.setProperty("rate", 170)
voice_engine.setProperty("volume", 0.8)

def voice_speak(text):
    def start_reading(text):
        # Starting voice speak
        voice_engine.startLoop(False); voice_engine.say(text); voice_engine.iterate()
        while voice_engine.isBusy():
            voice_engine.iterate()
        voice_engine.endLoop()
        # Voice speak finished

    def stop_reading(text): 
        # Sleeping for a second
        time.sleep(max(len(text) / 20.0 - 1, 0)  )
        # Stopping voice early
        voice_engine.stop()

    thread1 = threading.Thread(target=start_reading, args=(text,))
    thread2 = threading.Thread(target=stop_reading, args=(text,))
    thread1.start(); time.sleep(0.5); thread2.start()
    thread1.join(); thread2.join()

text_input = "Hello and welcome!"
text_input_2 = "We're happy that you're here"

voice_speak(text_input)
voice_speak(text_input_2)
