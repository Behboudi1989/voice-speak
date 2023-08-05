import time
import pyttsx3
import threading

voice_engine = pyttsx3.init()
voices = voice_engine.getProperty("voices")
voice_engine.setProperty("voice", voices[1].id)
voice_engine.setProperty("rate", 170)
voice_engine.setProperty("volume", 0.8)

def voice_speak(text):
    print("Starting voice speak...")
    voice_engine.startLoop(False)
    voice_engine.say(text)
    voice_engine.iterate()
    while voice_engine.isBusy():
        voice_engine.iterate()
    voice_engine.endLoop()
    print("Voice speak finished.")

def stop_early(text):
    time_to_sleep = max(len(text) / 20.0 - 1, 0)  
    print(f"Sleeping for {time_to_sleep} seconds.")
    time.sleep(time_to_sleep)
    print("Stopping voice early.")
    voice_engine.stop()

text_input = "Hello and welcome!"

thread1 = threading.Thread(target=voice_speak, args=(text_input,))
thread2 = threading.Thread(target=stop_early, args=(text_input,))

thread1.start()
time.sleep(0.5) 
thread2.start()

thread1.join()
thread2.join()
