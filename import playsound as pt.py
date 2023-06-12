import playsound as pt
import time
print("\t\t\t\t\tMUSIC PLAYER ", chr(128490),chr(128512))
time.sleep(5)

print("\t\tList of Songs " ,chr(128480))

time.sleep(2)

print("1)ANADHUN TITILE TRACK \n 2)CHALA JATA HOON \n 3)DIL NU \n 4)PUBG THEME SONG\n 5)JADUGAR \n 6)ZARA ZARA INSTRUMENTAL")

time.sleep(2)
while(True):
    r = int(input("Enter Song no. to play particular song  : " ))
    if r==1:
        pt.playsound("C:\\music\\Andhadhun Title Track Raftaar 128 Kbps.mp3")
    elif r==2:
        pt.playsound("C:\\music\\Chala Jata Hoon - Sanam (Band) 320 Kbps.mp3")
    elif r==3:
        pt.playsound("C:\\music\\Dil-Nu.mp3")
    elif r==4:
        pt.playsound("C:\\music\\English songs bgm.mp3")
    elif r==5:
        pt.playsound("C:\\music\\Jadugar Aisa Jadu Kar - Lofi - Paradox ! Hindi.mp3")
    elif r==6:
        pt.playsound("C:\\music\\Zara_Zara_Instrumental-Ringtonestar.Net.mp3")
        continue
    else:
        print("wrong input try again..!")
        continue
    print("Thank You ",chr(128512))
