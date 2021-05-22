from tkinter import *                   #pip install tkinter
from tkinter import filedialog as df    
from pygame import mixer                #pip install pygame

mixer.init()        #start-music-player
path=''
counter=0


def getname(name):
    name2=''
    for i in name[::-1]:
        if i=='/':
            break
        else:
            name2+=i
    return name2[::-1]

def getter():
    mixer.music.set_volume(w2.get()/100)

def player():
    global path
    if path:
        a=mixer.Sound(path)
        a=a.get_length()
        minute=str(int(a//60))
        if int(minute)<10:
            minute="0"+minute
        else:
            pass
        second=str(int(a%60))
        if int(second)<10:
            second="0"+second
        else:
            pass
        mtime.config(text=minute+":"+second)
        mixer.music.load(path)
        a=getname(path)
        status.config(text=a)
        mixer.music.play()
    else:
        status.config(text="Not Found")
def loader():
    global path
    path=df.askopenfilename()
def paused():
    global counter
    global path
    if path:
        if counter%2==0:
            mixer.music.pause()
            counter+=1
        else:
            mixer.music.unpause()
            counter+=1
    else:
        status.config(text="nothing to pause:|")
def stopping():
    global path
    if path:
        mixer.music.stop()
        path=''
        status.config(text="ok enter another")
        mtime.config(text="--:--")
    else:
        status.config(text="Nothing to stop")
        mtime.config(text="--:--")


app = Tk()  #root-app
app.geometry("200x200")
app.maxsize(200,200)
app.minsize(200,200)
app.title("Mp")
Label(app,text="volume",fg="blue").place(x=10,y=-5)
w2 = Scale(app, from_=0, to=100,bg="blue",bd="3", orient=VERTICAL)  #volume-rate
w2.set(100)
w2.place(x=5,y=15)
vol=Button(app, text='Set', command=getter) #change-volume-button
vol.place(x=10,y=125)

play=Button(app,text="Play",height=3,width=4,bg="red",fg="white",command=player)    #play-button
play.place(x=70,y=10)
load=Button(app,text="Load",height=3,width=4,bg="red",fg="white",command=loader)    #load-button
load.place(x=110,y=10)
quit=Button(app,text="Quit",height=3,width=4,bg="red",fg="white",command=app.destroy)   #quit-button
quit.place(x=70,y=70)
pause=Button(app,text="Pause",height=3,width=4,bg="red",fg="white",command=paused)  #pause-Button
pause.place(x=110,y=70)
clean=Button(app,text="Stop",height=4,width=4,bg="red",fg="white",command=stopping) #stop-button
clean.place(x=150,y=30)
status=Label(app,text="Welcome",bg='blue',fg='white',height=4,width=20)
status.place(x=50,y=130)
mtime=Label(app,text="--:--",bg="black",fg="white",height=2,width=3)
mtime.place(x=10,y=155)

mainloop()