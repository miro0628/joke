from tkinter import *
import jokehandler
jokehand = jokehandler.Jokehandler("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")


root = Tk()
root.title("Title")

root.geometry("1000x400")

textbox = Text(root, height=10, width=100, font="Helvetica")
header = Label(root, text="Dagens Joke")
header.config(font=("Helvetica", 14))

def clickButton():
    textbox.delete("1.0", "end")
    t_joke = jokehand.get_joke()
    textbox.insert(INSERT, t_joke)

button_getjoke = Button(text="Hämta skämt", padx=6, pady=5, command=clickButton)
butt_avsluta = Button(text="Avsluta", padx=6, pady=5, command=root.destroy)

header.pack()
textbox.pack()
button_getjoke.pack()
butt_avsluta.pack()


root.mainloop()