import pyttsx3
engine = pyttsx3.init()

engine.setProperty('voice', '''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0''')
engine.say('Hola mundo')
engine.runAndWait()
