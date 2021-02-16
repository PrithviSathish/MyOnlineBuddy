import tkinter
import fpdf
from fpdf import FPDF
from tkinter import filedialog

imagelist = filedialog.askopenfilenames()
print(imagelist)
pdf = FPDF()
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image, x=None, y=None, w=0, h=0)
pdf.output("yourfile.pdf", "F")
