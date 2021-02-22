""" My Online Buddy is a tool having various features from Converting to Images to PDF and Wikipedia searches. It is
designed as an overall pack for students attending online classes """

# ----- Imports -----
from tkinter import *
from fpdf import FPDF
from tkinter import filedialog
from tkinter import messagebox
import wikipedia
import warnings
from gtts import gTTS
import os


# Initialising root
root = Tk()
root.configure(background="gray")
root.geometry("1000x700")
root.title("MyOnlineBuddy | Home")


# ----- Creating the title -----
L = Label(root, text="My Online Buddy")
L.config(font=("Courier", 40))
L.pack()


# ----- Functions -----
def convert_pdf(event):

    # Get the PDF name
    name = input("Enter the name of the PDF: ")
    
    imagelist = filedialog.askopenfilenames()
    # print(imagelist)
    print("Converting to PDF...")
    try:
        pdf = FPDF()
        # imagelist is the list with all image filenames
        for image in imagelist:
            pdf.add_page()
            pdf.image(image, x=None, y=None, w=0, h=0)
        pdf.output(f"{name}.pdf", "F")

        messagebox.showinfo("PDF Converter | Success", "Success!")

    except:
        messagebox.showerror("PDF Converter | Error", "Failed! Invalid File types")
        print("Aborted.")


def search_wiki(event):

    # get the query
    q = input("Enter your search: ")
    result = wikipedia.search(q)

    warnings.catch_warnings()
    warnings.simplefilter("ignore")

    try:
        page = wikipedia.page(result[0], auto_suggest=False)
        title = page.title
        content = page.content
        print(title)
        print("-------------------------------------------------------")
        print(content)

    except wikipedia.exceptions.DisambiguationError as e:
        print("Sorry, the word " + q + " has many pages. Did you mean any one of these:")
        print(*e.options, sep = "\n")
        print("Aborted.")

    except wikipedia.exceptions.PageError as e:
        print("Sorry, the page doesn't exist")
        print("Aborted.")

    except:
        print("Please enter a valid word!")
        print("Aborted.")


def text_to_speech(event):

    # get the title and the text input
    title = input("Enter the title: ")
    Text = input("Enter your words: ")

    print("converting text to speech...")

    try:
        language = 'en'
        speech = gTTS(text=Text, lang=language, slow=False)
        speech.save(title + ".mp3")
        os.system("start " + title + ".mp3")
    except:
        messagebox.showerror("Text To Speech | Error", "Please enter valid words!")
  


# ----- Creating Background Image ------
canvas = Canvas(root, width=810, height=600)
canvas.pack()

# ----- Image to PDF -----
button1BG = canvas.create_rectangle(100, 500, 300, 450, fill="grey", outline="grey60")
button1TXT = canvas.create_text(195, 475, fill="darkblue", font=("courier", 20), text="Image to PDF")

canvas.tag_bind(button1BG, "<Button-1>", convert_pdf)
canvas.tag_bind(button1TXT, "<Button-1>", convert_pdf)

# ----- Wikipedia -----
button2BG = canvas.create_rectangle(700, 450, 500, 500, fill="grey", outline="grey60")
button2TXT = canvas.create_text(595, 475, fill="darkblue", font=("courier", 20), text="Wikipedia")

canvas.tag_bind(button2BG, "<Button-1>", search_wiki)
canvas.tag_bind(button2TXT, "<Button-1>", search_wiki)

# ----- Text To Speech -----
button3BG = canvas.create_rectangle(100, 570, 300, 520, fill="grey", outline="grey60")
button3TXT = canvas.create_text(200, 545, fill="darkblue", font=("courier", 15), text="Text to Speech")

canvas.tag_bind(button3BG, "<Button-1>", text_to_speech)
canvas.tag_bind(button3TXT, "<Button-1>", text_to_speech)


img = PhotoImage(file="Assets/TitlePage.png")
canvas.create_image(10, 10, anchor=NW, image=img)

root.mainloop()
