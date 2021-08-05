import pyttsx3
engine=pyttsx3
def larsen():
    engine.speak("please enter the number you want to print from ")
    x=int(input("Enter the numbers you want to print "))
    engine.speak("Enter the number up to which you want to print number ")
    y=int(input("Enter the ending digit "))
    engine.speak(x)
    print(x)
    while(x<=y):
        x=x+1      
        print(x)
        engine.speak(x)
        if x==y:
            break
try:
    larsen()
    engine.speak("Thats it boss")
except:
        engine.speak("Please dont type alphabeht or special case please type a number")
        print("The given number is not correct Please type number instead of alphabet ")

