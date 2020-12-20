from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import controller

src_files = ""
dest_files = ""

def setLabelText(label,text):
    label['text']= text

def src_clicked():
    global src_files
    src_files = filedialog.askopenfilename(filetypes = (("html files",".html"),("hbsfile",".hbs"),("tpl files",".tpl")))
    text = "Uploaded Source Files:\n1."+src_files
    setLabelText(upload_lbl,text)

def dest_dir_clicked():
    global dest_files
    dest_files = filedialog.askdirectory()
    text = "Destination Folder:\n1."+dest_files
    setLabelText(dest_lbl,text)

def dest_file_clicked():
    global dest_files
    dest_files = filedialog.askopenfilename(filetypes = (("html files",".html"),("hbsfile",".hbs"),("tpl files",".tpl")))
    text = "Destination File:\n1."+dest_files
    setLabelText(dest_lbl,text)


def change_action(event):
    print(combo.get())
    if(combo.get() == "Update Classes"):
        folder_btn.grid_remove()
        file_btn.grid()
    else:
        file_btn.grid_remove()
        folder_btn.grid()
        
def go_clicked():
    if(combo.get() == "Update Classes"):
        controller.doAction(src_files,dest_files,2)
    elif (combo.get() == "Add Auto Ids"):
        controller.doAction(src_files,dest_files,1)
    else:
        controller.doAction(src_files,dest_files,3)

window = Tk()
window.title("Auto Class Updater")

lbl = Label(window, text="Choose Action")
lbl.grid(column=2, row=0)
combo = Combobox(window)
combo['values']= ("Add Auto Ids", "Update Classes","remove Auto Ids")
combo.current(0)
combo.bind("<<ComboboxSelected>>", change_action)
combo.grid(column=3, row=0)

lbl = Label(window, text="Source Files")
lbl.grid(column=0, row=1)
btn = Button(window, text="Choose Files",command=src_clicked)
btn.grid(column=1, row=1)

lbl = Label(window, text="Save in")
lbl.grid(column=4, row=1)
folder_btn = Button(window, text="Choose Folder",command=dest_dir_clicked)
folder_btn.grid(column=5, row=1)
file_btn = Button(window, text="Choose File",command=dest_file_clicked)
file_btn.grid(column=5, row=1)
file_btn.grid_remove()


upload_lbl = Label(window, text="Uploaded Source Files:")
upload_lbl.grid(column=0, row=2,columnspan = 4)

dest_lbl = Label(window, text="Destination Folder:")
dest_lbl.grid(column=4, row=2, columnspan = 2)

btn = Button(window, text="GO!!!",command=go_clicked)
btn.grid(column=3, row=3)

progress_lbl = Label(window, text="Note:\n1. Add Auto Ids - result filename - *_idupdated.*\n2. Update Classes - will replace dest file \n3. remove auto Ids - result filename - *_idremoved.*")
progress_lbl.grid(column=0, row=4,columnspan=5)

window.mainloop()


