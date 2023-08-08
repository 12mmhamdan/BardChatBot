import pyttsx3
import sys


class TextToSpeechPrinter:
    def __init__(self):
        self.engine = pyttsx3.init()

    def __enter__(self):
        self.og_print = print

        def tts_print(*args, **kwargs):

            text = " ".join(str(arg) for arg in args)

            #speak text
            self.engine.say(text)
            self.engine.runAndWait()

        sys.stdout.write = tts_print

    def __exit__(self):
        # put back the og print
        sys.stdout.write = self.og_print