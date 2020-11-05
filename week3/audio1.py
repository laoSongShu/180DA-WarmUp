# code cited from the source given by the tutorials
# Remember to activate your virtual environment

# notes for setup:
# brew install portaudio
# pip3 install pyaudio

# conda install swig
# pip3 install pocketsphinx

import speech_recognition as sr
    
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio = r.listen(source)
                
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
