# This is a chat bot program:
import time

# This is a greeting section:
print("Welcome to Chat-bot".center(50))

def Time(a):
    if a==1 :
        h=int(time.strftime("%H"))
        return ("Good Morning Sir") if (h<12) else  ("Good Afternoon Sir") if (h<=17) else ("Good Evening Sir")
    elif a==2:   
        t=time.strftime("%H:%M:%S")
        return t
    else:
        pass    


def date():
    return time.strftime("%d/%m/%Y")



def Inp():
    return input("-> ").lower().strip()
    


def chat_logic():
        a=Inp()

        if a in ["hello","hi"]:
            print("Hello! " ,Time(1))
            print("What's your name ")
            name=Inp()
            print(f"Nice to meet you {name}")
            
            a=Inp()

            while (a != "bye" and a !="exit" and  a!="quit"):
                if a == "help":

                        print(   "Bot: \n Available commands:\n- time\n- date\n- how are you\n- what is your name\n- bye / exit / quit")
                        a=Inp()
                elif a in["time"]:
                        print(f"Currently it's = {Time(2)}")        
                        a=Inp()
                    
                elif a in ["date"]:
                        print(f"today is = {date()} ")
                        a=Inp()
                
                elif a in ["how are you"]:
                        print("I am doing Great how about you")
                        a=Inp()
                elif a in ["what is your name"]:
                        print("I am Python Chat-bot made by Anant Kumar")
                        a=Inp()
                
                else:

                    print("Sorry I didn't understand that \nfor more option Enter \"help\". ") 
                    a=Inp()

            print("Goodbye! Have a nice day.")




chat_logic()