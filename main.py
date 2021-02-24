"""
My Online Buddy is a tool having various features from Converting to Images to PDF and Wikipedia searches. It is
designed as an overall pack for students attending online classes
"""


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
    # print("Converting to PDF...")
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
        save = messagebox.askquestion("Wikipedia", "Do you want to save the content as a file?")

        if save == "yes":
            # print("Yes")
            file = open((str(title) + ".txt"), "w", encoding='utf-8')
            file.write(content)
            messamessagebox.showinfo("Wikipedia | Success", "Saved content as File successfully")
        else:
            print(title)
            print("-------------------------------------------------------")
            print(content)


    except wikipedia.exceptions.DisambiguationError as e:
        messagebox.showinfo("Error", "Sorry, the word " + q + " has many pages. Did you mean any one of these:\n\n" + str(e.options))
        # print(*e.options, sep = "\n")
        print("Aborted.")

    except wikipedia.exceptions.PageError as e:
        messagebox.showerror("Error", "Sorry, the page doesn't exist")
        print("Aborted.")
    
    
    except:
        messagebox.showerror("Error", "Please enter a valid word!")
        print("Aborted.")
    

def text_to_speech(event):

    # get the title and the text input
    title = input("Enter the title: ")
    Text = input("Enter your words: ")

    # print("converting text to speech...")

    try:
        language = 'en'
        speech = gTTS(text=Text, lang=language, slow=False)
        speech.save(title + ".mp3")
        os.system("start " + title + ".mp3")
        messagebox.showinfo("Text To Speech | Success", "Converted successfully")
    except:
        messagebox.showerror("Text To Speech | Error", "Please enter valid words!")


def to_do_list(event):
    d = {}
    # Main program Loop
    ch = 0
    while ch != 4:

      # Create the drop-down menu
      print("\n1. Add new task\n2. Finished a task\n3. Show all my tasks\n4. Exit")
      ch = int(input("Enter your choice: "))

      if ch == 1:
        # When new task is added...
        task_title = input("Enter the title for your task: ")
        if task_title not in d.keys():
            task_des = input("Enter the description for your task: ")
            d[task_title] = task_des
            change = True
            messagebox.showinfo("To Do List", "New task added")
            # f.write(task_title + ':' + task_des + '\n')
        else:
            messagebox.showerror("To Do List", "Task already exists")

      elif ch == 2:
        # When a task is finished...
        task_title = input("Enter the title of the task that you completed: ")
        if task_title in d.keys():
            del d[task_title]
            change = True
            messagebox.showinfo("To Do List", "Task removed")
        else:
            messagebox.showerror("To Do List", "Task doesn't exist")

      elif ch == 3:
        # Printing the dictionary
        print('\n\n')
        for key in d:
            print(key, end="\t\t")

        print()
        for value in d.values():
            print(value, end = "\t\t")

        print('\n\n')

      elif ch == 4:
        # Loop over, quit
        messagebox.showinfo("To Do List", "Task Complete")
        break

      else:
          messagebox.showerror("To Do List", "Enter a Valid number!")



def exit():
    ex = messagebox.askquestion("Exit", "Do you want to exit the application?")
    if ex == "yes":
        root.destroy()
    else:
        pass
  


# ----- Creating Background Image ------
canvas = Canvas(root, width=810, height=600)
canvas.pack()

# ----- Image to PDF -----
button1BG = canvas.create_rectangle(100, 500, 300, 450, fill="grey", outline="grey60")
button1TXT = canvas.create_text(195, 475, fill="darkblue", font=("courier", 15), text="Image to PDF")

canvas.tag_bind(button1BG, "<Button-1>", convert_pdf)
canvas.tag_bind(button1TXT, "<Button-1>", convert_pdf)


# ----- Wikipedia -----
button2BG = canvas.create_rectangle(700, 450, 500, 500, fill="grey", outline="grey60")
button2TXT = canvas.create_text(595, 475, fill="darkblue", font=("courier", 15), text="Wikipedia")

canvas.tag_bind(button2BG, "<Button-1>", search_wiki)
canvas.tag_bind(button2TXT, "<Button-1>", search_wiki)


# ----- Text To Speech -----
button3BG = canvas.create_rectangle(100, 570, 300, 520, fill="grey", outline="grey60")
button3TXT = canvas.create_text(200, 545, fill="darkblue", font=("courier", 15), text="Text to Speech")

canvas.tag_bind(button3BG, "<Button-1>", text_to_speech)
canvas.tag_bind(button3TXT, "<Button-1>", text_to_speech)


# ----- To Do List -----
button4BG = canvas.create_rectangle(700, 520, 500, 570, fill="grey", outline="grey60")
button4TXT = canvas.create_text(595, 545, fill="darkblue", font=("courier", 15), text="To-Do-List")

canvas.tag_bind(button4BG, "<Button-1>", to_do_list)
canvas.tag_bind(button4TXT, "<Button-1>", to_do_list)

# ----- Creating exit button -----
exit = Button(root, text="       Exit      ", bd='10', bg="red", command= exit)
exit.pack(side = 'bottom', anchor=SE)

img = PhotoImage(file="Assets/TitlePage.png")
canvas.create_image(10, 10, anchor=NW, image=img)


root.mainloop()
