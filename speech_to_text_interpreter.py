from beepy import beep
import speech_recognition as sr
import builtins



def play_sound():
    beep(sound=1)

class SpeechToTextInterpreter:
    def __init__(self):
        self.r=sr.Recognizer()

    def read_line(self, *arg):
        while True:
            with sr.Microphone() as source:
                play_sound()
                audio = self.r.record(source, 4)
                print('\a')
            try:
                text = self.r.recognize_google(audio)
                if text:
                    return text

            except sr.UnknownValueError:
                print("Sorry I dont understand your question")
            except sr.RequestError:
                print('Sorry, I had trouble connecting. Try Again')
            except Exception:
                print("Try again, don't know what happened")

    def __enter__(self):
        self.og_input = builtins.input
        builtins.input = self.read_line

    def __exit__(self, exc_type, exc_value, exc_trace):
        builtins.input == self.og_input