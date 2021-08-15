import speech_recognition as sr
import webbrowser
import time
import pyttsx3
from time import ctime

# Identifires
r = sr.Recognizer()
assistant_name = 'Persi'  # Name of the Voice Assistant
engine = pyttsx3.init()   # init function to get an engine instance for the speech synthesis
logger = True 

# Functions
def record_audio(ask = False):
    with sr.Microphone() as source:
        # If a Question is Passed persi_speak it
        if ask:
            persi_speak(ask)
        
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            persi_speak('Sorry, Did Not Get That')
        except sr.RequestError:
            persi_speak('Sorry, My Services are Down currently')
        return voice_data

def persi_speak(audio_string):
    if(logger==True):
        print(audio_string)
    engine.say(audio_string)
    engine.runAndWait()

# Text To Speach gTTS
# def persi_speak(audio_string):
#     tts = gTTS(text=audio_string, lang='en')
#     r = random.randint(1, 1000000)
#     audio_file = 'audio-' + str(r) + '.mp3'
#     tts.save(audio_file)
#     playsound.playsound(audio_file)
#     print(audio_string)
#     os.remove(audio_file)


# Custom Functions
def custom_open_func():
    persi_speak('What do you want to open?')
    open_term_voice_data = record_audio()
    if 'my portfolio' in open_term_voice_data:
        webbrowser.get().open('https://sayanresumev2.web.app/')
        persi_speak('Opened Sayan\'s portfolio website.')
    if 'company' in open_term_voice_data:
        webbrowser.get().open('https://ncdcstaffcoop.org/ncdc/')
        persi_speak('Opened company\'s website.')
    else:
        persi_speak('Sorry could not get it.')
# CPU
def respond(voice_data):
    if 'open' in voice_data:
        custom_open_func()
    if 'what is your name' in voice_data:
        persi_speak('My name is '+assistant_name)
    if 'what is the time' in voice_data:
        persi_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to Search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        persi_speak('Here is what I found for : '+search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        persi_speak('Here is the location for : '+location)
    if 'exit' in voice_data:
        exit()


# Main
time.sleep(1)
persi_speak('How Can I Help You ?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    persi_speak('Any other thing you want me to do ?')