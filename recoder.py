#install tkinter, sounddevice, scipy, time, wavio
from tkinter import * 
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as w

# background
root = Tk()
root.geometry("400x400+400+80")
root.resizable(False, False)
root.title("My Voice Recorder")
root.configure(background="#F5F5F5")

# record function
def Record():
    freq = 44100
    dur = int(duration.get())
    recording = sound.rec(dur*freq,
                          samplerate = freq, channels = 2)
    try:
        temp = int(duration.get())
    except:
        print("Please enter the right value")

    while temp>0:
        root.update()
        time.sleep(1)
        temp=temp-1

        if(temp==0):
            messagebox.showinfo("Time Countdown","Time's up")
        Label(text=f"{str(temp)}", font = "perpetua 25", width = 4, background = "#F5F5F5").place(x=160, y=320) 
    
    sound.wait
    write("Recording.wav",freq,recording)

#icon
image_icon = PhotoImage(file = "CB\Voice Recorder\image.png")
root.iconphoto(False, image_icon)

#logo
photo = PhotoImage(file= "CB\Voice Recorder\image.png")
myimage = Label(image=photo)
myimage.pack(padx=5,pady=25)

#defining labels
Label(text="Voice Recorder", font = "forte 28 bold", background = "#F5F5F5", fg = "navy").pack()

duration = StringVar()

Label(text = "Enter time in seconds ", font = "perpetua 18 italic", background = "#F5F5F5", fg= "navy").pack()
entry = Entry(root, textvariable = duration, font = "Times 15 bold", width = 20).pack()

record = Button(root, font="perpetua 18 bold", text = "Record", bg = "#0A1172", fg = "white", border = 0, command= Record).pack(pady = 25)

#running mainloop
root.mainloop()