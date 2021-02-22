import wikipedia
import warnings

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
except wikipedia.exceptions.PageError as e:
    print("Sorry, the page doesn't exist")
except:
    print("Please enter a valid word!")

    import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    image1 = Image.open(import_file_path)
    im1 = image1.convert('RGB')


browseButton = tk.Button(text="     Select File     ", command=getFile, bg='green', fg='white',
                         font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton)


def convertToPdf():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    im1.save(export_file_path)


saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='green', fg='white',
                         font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton)


def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='Exit Application', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()