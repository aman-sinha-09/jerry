from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Jerry : Wait For Some Seconds... ")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting The Jerry : Wait For Few Seconds More... ")
from Main import MainTaskExecution

for i in range(3):
    Speak("Please Tell The Password To Start Jerry")
    a=MicExecution()
    a=str(a)
    pw_file = open("DataBase\password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        Speak("Welcome Sir, Please Clap To Load Me Up")
        break

    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        Speak("Wrong password")
        Speak("Try again please")

def Mainexecution():
    Speak("Hello Sir")
    Speak("I'm Jerry, I'm Ready To Assist You Sir")

    while True:
        Data=MicExecution()
        Data=str(Data).replace(".","")

        valuereturn=MainTaskExecution(Data)
        if valuereturn==True:
            pass

        elif len(Data)<3:
            pass
  
        elif 'offline' in Data:
            Speak('as you wish sir')
            quit()
            
        else:
            Reply=ReplyBrain(Data)
            Speak(Reply)

def clapdetect():
    query=Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        Mainexecution()
    else:
        pass

clapdetect()