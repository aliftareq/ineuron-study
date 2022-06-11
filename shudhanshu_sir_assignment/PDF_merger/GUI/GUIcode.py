import logging

logger = logging.getLogger()
log = logging.getLogger(__name__)

# importing library

from tkinter import *
from PIL import Image, ImageTk
import  os
import PyPDF2
import re
import datetime

from PyCode.function import merge_pdf
from PyCode.function import get_all_files


# GUI function

# submit button action
def submit_click():
    logging.info("submit button clicked")
    pdf_file_output.delete(0.0, END)
    all_file_output.delete(0.0, END)

    folder_path = folder_path_text.get()
    logging.info("Entered folder path is: " + folder_path)

    logging.info("Calling get all function")
    all_file_list, pdf_file_list = get_all_files(folder_path)

    logging.info("printing all file list")
    for file in all_file_list:
        all_file_output.insert(END, f"{file}\n")

    logging.info("printing pdf file list")
    for file in pdf_file_list:
        pdf_file_output.insert(END, f"{file}\n")


def pdf_click():
    logging.info("PDF Merge button clicked")
    logging.info("calling get_all_file function")
    folder_path = folder_path_text.get()
    logging.info("Entered folder path is: " + folder_path)
    all_file_list,  pdf_file_list = get_all_files(folder_path)
    logging.info("Merge PDF function")
    merge_pdf(folder_path, pdf_file_list)
    pdf_file_output.delete(0.0, END)
    all_file_list, pdf_file_list = get_all_files(folder_path)
    logging.info("uploading pdf list after Merging")
    for file in pdf_file_list:
        pdf_file_output.insert(END, f"{file}\n")

# clear button function


def clear_click():
    logging.info("Clear button clicked")
    pdf_file_output.delete(0.0, END)
    all_file_output.delete(0.0, END)


# initializing Tk window

window = Tk()
window.title("PDF Merger")
window.configure(background="skyblue")
window.geometry("900x600")

# adding title image

title_img = Image.open("pdf banner.jpg")
photo = ImageTk.PhotoImage(title_img)
Label(image=photo).grid(row=0, column=1)


# title_img= PhotoImage(file="title.png") # To be used when only running from GUICode.py file

# title_img = PhotoImage(file="pic.PNG")
# Label(window, image=title_img, bg="black").grid(row=0, column=0, sticky="w")

# creating Label for entering path

Label(window, text="Enter path: ", bg="black", fg="white",
      font="none 12 bold", width=10).grid(row=1, column=0, sticky="e")

# adding text box for folder path entry

folder_path_text = Entry(window, bg="white", width=60)
folder_path_text.grid(row=1, column=1)

# Adding submit Button

submit_button = Button(window, text="Submit", width=8, relief=SOLID, command=submit_click, pady=10)
submit_button.grid(row=1, column=2, sticky="w")


# print All file list

Label(window, text="\n Available files in entered folder are as below: ", bg="white", fg="black",
      font="Arial 10 bold").grid(row=3, column=0, sticky="w")
all_file_output = Text(window, width=50, height=20, wrap=WORD, bg="white", fg="black", font="Arial, 10")
all_file_output.grid(row=4, column=0, sticky="w")

# print pdf file list

Label(window, text="\n Available PDF files are below:  ", bg="white", fg="black",
      font="Arial 10 bold").grid(row=3, column=1, sticky="w")
pdf_file_output = Text(window, width=50, height=20, wrap=WORD, bg="white", fg="black", font="Arial 10")
pdf_file_output.grid(row=4, column=1, sticky="w")

# adding button for pdf merger

pdf_button = Button(window, text="Merge PDF and update list", width=20, relief=SOLID,
                    command=pdf_click, pady=10)
pdf_button.grid(row=4, column=2, sticky="w")

# adding button for clear

clear_button = Button(window, text="Clear all", width=12, relief=SOLID,
                    command=clear_click, pady=10)
clear_button.grid(row=5, column=2, sticky="w")


# running GUI
logging.info("Opening GUI Window")
window.mainloop()
logging.info("Closing GUI Window")
