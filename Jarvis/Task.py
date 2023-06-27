import datetime
from Speak import say
import wikipedia
import pywhatkit


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    say(time)

def Date():
    date = datetime.date.today()
    say(date)


def day():
    day = datetime.datetime.now().strftime("%A")
    say(day)


def Wikipedia(tag,query):
    name=str(query).replace("","")
    result=wikipedia.summary(name)
    say(result)



def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()

   
    elif "day" in query:
        day()


def InputExecution(tag,query):

    if "wikipedia" in tag:
        name=str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        result=wikipedia.summary(name)
        print(result)
        say(result)

    elif "google" in tag:
            query=str(query).replace("google","")
            query=query.replace("search","")
            pywhatkit.search(query)
           

