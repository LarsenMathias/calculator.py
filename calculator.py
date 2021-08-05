import pyttsx3 as engine 
engine.speak("Enter the first value ")
x=int(input("Enter the first value "))
engine.speak("Enter the second value ")
y=int(input("Enter the second value "))
def add():
        operation=x+y
        engine.speak(operation)
        round(4,operation)
        print(operation)
        
def subtract():
        operation=x-y
        engine.speak(operation)
        round(4,operation)
        print(operation)
def mulitply():
        operation=x*y
        engine.speak(operation)
        round(4,operation)
        print(operation)
def divide():
        operation=x/y
        engine.speak(operation)
        print(operation)
        round(4,operation)
engine.speak("If you want to add then press 1, if you want to subtract then press 2, if you want to multiply press 3, if you want to divide press 4 ")
number=input("If you want to add then press 1 if you want to subtract then press 2 if you want to multiply press 3 if you want to divide press 4 ")
if number=="1":
        try:
            add()
        except:
            print("THe given value is not correct ")
            engine.speak("Please chose numbers among 1,2,3,4")
if number=="2":
        try:
            subtract()
        except:
            print("Enter the correct number ")
            engine.speak("Please chose numbers among 1,2,3,4")
if number=="3":
        try:
            mulitply()
        except:
            print("The given number is not correct ")
            engine.speak("Please chose numbers among 1,2,3,4")
if number=="4":
        try:
            divide()
        except:
            engine.speak("Please chose numbers among 1,2,3,4")
            print("The given number is not corrrect ")
