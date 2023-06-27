import pyttsx3 







def say(Text):
    print(f"A.i : {Text}")
    engine= pyttsx3.init("sapi5")
    voices =engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    engine.say(text=Text)
    engine.runAndWait()
    print("     ")


# say("hello how are you ")