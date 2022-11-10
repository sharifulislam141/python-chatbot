from tkinter import *
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == 'how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i am fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif (e.get() == "are you boy or girl?"):
        text.insert(END, "\n" + "Bot: I am a beautiful girl ")
    elif (e.get() == "are you single?"):
        text.insert(END, "\n" + "Bot: YES i am")
    elif (e.get() == "i love you"):
        text.insert(END, "\n" + "Bot: Zuta Chinos? Nijer chehara deksos aynai??")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='black', fg='green')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='deeppink', fg='white', width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('DARKHUNTER CHAT BOT')
root.mainloop()
