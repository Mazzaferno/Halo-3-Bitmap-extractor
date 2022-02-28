import tkinter              
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
from tkinter import filedialog
import subprocess
import os.path
import base64
from functools import partial
import pathlib
from PIL import Image 
tiff = 0
output = 'none'
def dir_snip(boo):
    global output
    global filesel
    dir = os.getcwd()
    if boo == 'i':
        os.chdir("data")
        filesel = filedialog.askopenfilename(initialdir = os.getcwd(),title="select file",filetypes=(("TIFF",".TIF"), ("all files", "*.*")))
        
    if boo == 'e':
        os.chdir("tags")
        filesel = filedialog.askopenfilename(initialdir = os.getcwd(),title="select file",
        filetypes=(("Bitmap",".bitmap"), ("all files", "*.*"))) ##os.getcwd = current directory


    filesel = filesel.replace ('/','\\')  ##why does python hate backslash in strings
    output = filesel.replace(dir,'')[6:len(filesel)] ## https://stackoverflow.com/questions/42798967/how-to-subtract-strings-in-python/42799034
    if boo == 'e':
        output = output.replace(".bitmap",'')
    Dir_Entry_box.delete(0, END)
    Dir_Entry_box.insert(0, output)
    os.chdir("..")
    
def export():
    global xport
    global filesel
    global tiff
    selection_extention = StringVar.get(xport)
    if os.path.isdir("data/bitmap_exports"):
        if selection_extention == "tiff":
            print("ITS AN PNG DUMMY ITS AN PNG DUMMY ITS AN PNG DUMMY ITS AN PNG DUMMY ")
            tiff = 1
            convert = os.path.basename(filesel)
            convert = convert.replace('.bitmap','')
            selection_extention = "dds"
        debugwindow.delete(1.0,END)
        #print("todays command: tool " +"export-bitmap-dds "+ output + " data\\")
        #os.systesubm("tool " +"export-bitmap-dds "+ output + " data\\")
        os.startfile(r"data\bitmap_exports")

        complie = subprocess.Popen("tool export-bitmap-"+selection_extention+" "+ output + " data\\bitmap_exports\\", stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE ,shell=True)
        # fr"tool export-bitmap-{selection_extention} output data\bitmap_exports\\"
        complie.wait()
        outcome = complie.stdout.readlines()
        #print(outcome)
        debugwindow.delete(1.0,END)
        debugwindow.insert(END, outcome)
        if tiff == 1:
            convert=convert+'_00'+'.dds'
            path=(os.path.join('data','bitmap_exports',convert))
            im = Image.open(path)
            rgb_im = im.convert("RGBA")
            path = path.replace('.dds','')
            rgb_im.save(path+".Tiff")
            convert=convert.replace('.dds','.TIFF')
            debugwindow.insert(END,"------File-converted-and-saved[ "+convert+" ]--------")

        #print(StringVar.get(xport))
        mainloop()
    else:
        os.makedirs("data/bitmap_exports")
        command=export()

def bitimp():
        debugwindow.delete(1.0,END)
        complie = subprocess.Popen("tool " +"bitmap_single "+ output, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE ,shell=True)
        complie.wait()
        outcome = complie.stdout.readlines()
        print(outcome)
        debugwindow.insert(END, outcome)

window = tkinter.Tk()
window.title("Bitmap extractor")
tabControl = ttk.Notebook(window,)


##The Base64 icon version as a string
icon = \
    'AAABAAEAKioAAAEAIAAIHQAAFgAAACgAAAAqAAAAVAAAAAEAIAAAAAAAkBsAABMLAAATCwAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACOCq7/tx1G/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAvh2y/4gASfMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjwqu//5yjf//f4D//3+A/49OC/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACRTfP//3+A//9/gP/8bGz/jgtS/////wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJUMsv//f4D//3+A//9/gP//f4D//3+A//97e/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD/f4H//4CA//+AgP//gID//4CA//+AgP+TDU//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wCWDbP//3+A//9/gP//f4D//3+A//9/gP//f4D//4CA//+AgP93OQH9////AP///wD///8A////AI9Q9P//gID//4CA//+AgP//gID//4CA//+AgP//gID//39//5QNTv////8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AAAA+CT/f4D//3+A//9/gP//f4D//3+A//9/gP//gID//4CA//+AgP/8bW3/////AP///wD///8A////AP53if//gID//4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP8BAQEC////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD+i4v//3+A//9/gP//f4D//3+A//+AgP//gID//4CA//+AgP//gID/j08M/////wD///8AkE/0//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID//4CA//uXaf////8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wCNr/T8/3+A//9/gP//f4D//4CA//+AgP//gID//4CA//+AgP//gID//3p6/////wD///8A/36C//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//f4D//4OE/26PAfr///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A/4KC//9/gP//gID//4CA//+AgP//gID//4CA//+AgP//gID//4CA/3MbAfuYSer//4CA//+AgP//gID//4CA//+AgP//gID//7G8//9/gP//l6L/7qxT/////wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8AkLH0//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID//4CA///L4P//q7///4CA//+AgP//gID//4CA///C4P//f4D//4CA//+zy///vtv/FUIBwP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP6IiP//gID//4CA//+AgP//gID//4CA//+AgP//gID//6Cl//+30f//mJ3//4CA//+AgP//r7j//4CA//+AgP//gID//5qn//9/gP/9kW//////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wCKAIL4////AP///wD///8A////AP///wD///8A////AI+w9P//gID//4CA//+AgP//gID//4CA//+AgP//gID//4GD//+Xov//gID//3+A//+AgP//f4D//4KE//+muP//tc7//6a4//+zy/+AogD+////AP///wD///8A////AP///wD///8A////AIQBb/////8A////AP///wD///8AAAAAAP///wD/f4D//3+A//9/gP/+d3f/owtf/44Ea/////8A////AP///wD/gID//4CA//+AgP//gID/+pdp/4DrTP7///8A////AP///wD///8A////AP///wCk+tz//Z2k//+AgP//sMf//3+A//+twv////8A////AP///wCOA5X/pQyi//+32P//gID//4CA//+AgP////8A////AP///wD///8AAAAAAI9o/P//f4D//3+A//9/gP//gID//4CA//+AgP//gID//39//9UjiP//gID//4CA//+AgP//gID/////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP+vxv//f4D//63D//+muP/VIX7//4CA//+Hi///f4D//3+A//+AgP//gID//4CA//+AgP+GYgH/////AP///wD///8AAAAAALJW7f//f4D//3+A//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP8ARwCX////AP///wD///8A////AP///wD///8A////AP///wD///8A////ADyCm97/q7///5qn//+muP//s8z//7LK//+LkP//pLT//83l//+AgP//gID//4CA//+AgP+oXA3/////AP///wD///8AAAAAAP9/gP//f4D//4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID//4CA/5HOHf////8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wCi3vH//3+A//9/gP//gID//7bP//9/gP//yOn//4CA//+AgP//gID//4CA//+AgP//e3v/////AP///wD///8AAAAAAP9/gP//gID//4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/m9Ai/////wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8At+j2//+Sm///maX//4CA//+Jjv//gID//4CA//+AgP//gID//4CA//+AgP//gID/////AP///wD///8Ajmj8//+AgP//gID//4CA//+AgP//gID//4CA//9/gP//gID//4CA//+AgP/xqVf/////AP///wD///8Au6v7//+AgP//f4D//4CA//+js///jpb//3+A//9/gP//t9D/omQY/////wD///8A////APu3xf//gID//3+A///D2///gID//4CA//+AgP//gID//4CA//+AgP//gID/gV8B/v///wD///8AsFfu//+AgP//gID//4CA//+AgP//gID//5qc//+Kj///io///4CA//+AgP+XigT/////AP///wD///8AyrT5//++2///f4D//4CA//+Bg///gIH//4CA//+pvP//gID/sokl/////wD///8A////AKGb/P//ts///7K6//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/p1wN/////wD///8A/3+B//+AgP//gID//4CA//+AgP//gID//6Oz//+ChP//f4D//4CA//+AgP+oayz/////AP///wD///8AvYDv//+Mkv//ssr//3+A//+NlP//f4D//3+A//+AgP//ssr/tZRD/////wD///8A////ALBl8v//f4D//3+A//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID//3x2/////wD///8AAAAAApT7mf/V0a///4CA//+AgP//gID//3+A//+41P//gID//46Q//+AgP//ipD/////AP///wD///8AvYDv//9/gP//gID//3+A//+Eh///jJP//3+A//+Pl///f4D/r38J/////wD///8A////AP9/gP//vsX//4CA//+AgP//gID//4CA//+AgP//gID//4CA/9DWUf+T+2j/////AP///wD///8AAAAAAP///wD///8A////AP///wC7/uj/xvXl//+AgP//sMf//3+A//9/gP//p7n/////AP///wD///8AvYDv//+AgP//ttD//3+A//+Unf//sMf//42U//+AgP//f4D/uJ1d/////wD///8A////AP+AgP//gID//4CA//+AgP//gX//s+1Y/4/8av////8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A/6Gx//+71v//gID/i2cB/////wD///8AzsT8//9/gP//qr7//8Tk//+AgP//i5H//4CA//+Qmf//udT/s4wr/////wD///8Aj2r8//+AgP//gID//4CA/////wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wDTPMP//63C//+Bgv//gID/o10L/////wD///8AyrT5//+Dhv//qLv//4CA//+uxP//f4D//4CA//+AgP//f4D/t5tW/////wD///8Aq1rx//+AgP//gID//4CA/8k3N/////8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8AZQGg9/9+gv//gID//6W2//+Jjf//rsP//5il/////wD///8Azb36//+/3f//sMf//4OG//+AgP//g4X//3+A///B3///gID/s44y/////wD///8A/4CA//+AgP//gID//4CA//+AgP//fHz/PwEB4P///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wCRGcr//4CA//+AgP//gYP//4CA//9/gP//gID//4CA/////wD///8Ay7T4//+AgP//jJP//63C//+ChP//gID//3+A//+AgP//gID/r38J/////wD///8A/4CA//+AgP//gID//4CA//+AgP//gID//4CA/5EaNv////8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AMIyzP//vtr//6Kx//9/gP//iY7//4CA//+AgP//gID//4SH/////wD///8Av3/u//9/gP//gID//4mN//+AgP//gYP//5ej//+TnP//p6b/r4AK/////wD///8A/4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP+5LzH/////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A9l+h//9/gP//vNj//6W4//+AgP//maT//4CA//+swf//gID//4CA/////wD///8Av3/u//+AgP//lZ///73Y//+AgP//qLz//4CA///P5f//gID/r4AK/////wD///8A/4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/71VV/////wAAAAAAAAAAAP///wD///8AAAAAAP///wDjlsv//4CA//+AgP//yOn//5eh//+Ijf//f4D//7bQ//+IjP//f4D//4CA/////wD///8AzL76//+AgP//f4D//3+A//+AgP//qbz//4eH//+AgP//gID/r4AK/////wD///8A/4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID//3+A/86UHf8AAAAAAAAAAP///wD///8AAAAAAP///wAECQ0I/6m9//+Bg///io///5CY//+Plv//scj//3+A//+AgP//nav//4CA/////wD///8Ay7n5//+AgP//r8T//4yT//+AgP//tb7//4CA//+AgP//gID/r4AK/////wD///8A/4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID//4B//////wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8AGGqIwv+1vv//udP//7LJ//+AgP//jpX//4CA//9/gP//g4b//3+A/////wD///8AvX/v//+51P//f4D//4CA//9/gP//gID//4CA//+AgP//gID/r4AK/////wD///8A/4CA//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//f4D/AC4APf///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AJbP4P//tM3//5qn//+40v//iI3//3+A//+AgP//h4v/oNdl/////wD///8AzLz6//+AgP//gID//3+A//+AgP//gID//4CA//+AgP//gID/r4AK/////wD///8Al87h//+AgP//gID//4CA//+AgP//gID//4CA//+AgP+Uzh3/////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wCe0d3//7TM//+yyP//gID//7jT//+Af/8+qTHW////AP///wD///8AvYDv//9/gP//gID//4CA//+AgP//gID//4CA//+AgP//gID/r4AK/////wD///8A////AGG7nPX/gID//4CA//+AgP//gID//4CA/5rQIP////8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A1MjI//+cqv//goT/xcw5/////wD///8A////AP///wD///8A06/2//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/r4AK/////wD///8A////AP///wD///8A8qen//+AgP//gID/xMw0/////wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////APuVlf/J8dH/////AP///wD///8A////AP///wD///8AvYDv//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/r4AK/////wD///8A////AP///wD///8A////AKXb0P/4nWP/////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AvYDv//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/r4AK/////wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AvYDv//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/r4AK/////wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AvYDv//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/r4AK/////wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AvYDv//+AgP//gID//4CA//+AgP//gID//4CA//+AgP//gID/r38J/////wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8AvYDv//+AgP//f4D//3+A//9/gP//f4D//3+A//9/gP//f4D/r38J/////wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wAAAAAAAAAAAP///wD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlsDr//9/gP//f4D//3+A//9/gP//f4D//3+A//9/gP//f4D/lL0R/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD//////8AAAP/+f5//wAAA//g/B//AAAD/4D8B/8AAAP+AHgB/wAAA/wAeAD/AAAD/gAwAf8AAAP+ADAB/wAAA/8AAAP/AAAD/wAAA/8AAAP/gAAH/wAAA7+AAAf3AAADgcD8DgcAAAMAA/8AAwAAAwAD/wADAAADAAf/gAMAAAMAD//AAwAAAgAcAOABAAACABwA4AEAAAIAHADgAQAAAgAcAOADAAAD8BwA4D8AAAP/DADD/wAAA/4MAMH/AAAD+AwAwH8AAAPwDADAPwAAA+AMAMAfAAADwAwAwA8AAAOADADABwAAA4AMAMAPAAADwAwAwA8AAAPgDADAHwAAA/AcAOA/AAAD+HwA+H8AAAP8/AD8/wAAA//8AP//AAAD//wA//8AAAP//AD//wAAA//8AP//AAAD//wA//8AAAP//AD//wAAA///////AAAA='
icondata= base64.b64decode(icon)
## The temp file is icon.ico
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()
window.wm_iconbitmap(tempFile)
## Delete the tempfile
os.remove(tempFile)


#window.iconbitmap("ico.ico")

tab1 = ttk.Frame(tabControl,)
tab2 = ttk.Frame(tabControl,)
bugframe =ttk.Frame(window,)
bugframe.pack(side=BOTTOM,expand=0,)
entframe = ttk.Frame(window)
Dir_Entry_box = ttk.Entry(entframe, width=55,justify=LEFT,)

debugwindow = Text(bugframe, height=12,width=60,bg="#9db6b6",fg="black",bd=3)
debugwindow.config(state=NORMAL)
entframe.pack(expand=1,fill=BOTH)
tabControl.add(tab1, text ='export')
tabControl.add(tab2, text ='import')

tabControl.pack(expand=1,fill=BOTH,side=TOP)

ttk.Label()

ttk.Label(tab1, 
          text = "Export-bitmap-<type>").grid(column = 1, 
                               row = 0,
                               padx = 0,
                               pady = 0)  
ttk.Label(tab2,
          text ="Import-bitmap").grid(column = 1,
                                    row = 0, 
                                    padx = 0,
                                    pady = 0)
#radio buttons


xport = StringVar(tab1,"dds")
##=================-Radio-==-Buttons-=======================================================##
dds=tkinter.Radiobutton(tab1, text="dds",variable=xport, value="dds",).grid(column=1,row=1)
pfm=tkinter.Radiobutton(tab1, text="tga",variable=xport, value="tga",).grid(column=2,row=1)
pfm=tkinter.Radiobutton(tab1, text="pfm",variable=xport, value="pfm",).grid(column=3,row=1)
pfm=tkinter.Radiobutton(tab1, text="tiff",variable=xport, value="tiff",).grid(column=1,row=2)
##===========================================================================================##
selection = 'directory'
Dir_Entry_box.grid(column=0,row=1)
Dir_Entry_box.insert(0, selection)
debugwindow.grid(row=3)
ttk.Button(tab1, text="Select file", command=partial(dir_snip,'e')).grid(column = 0, row = 1,)
ttk.Button(tab2, text="Select file", command=partial(dir_snip,'i')).grid(column = 0, row = 1,)

ttk.Button(tab1, text="export",command=export).grid(column = 0, row = 2)
ttk.Button(tab2, text="import",command=bitimp).grid(column = 0, row = 2)


ttk.Label(bugframe, text='debug window',justify=LEFT).grid(column=0, row=0,)


debugwindow.insert(END, '''     _  --  _   
    / \|  |/ \  
    \  |  |  /  
   --  |  |  --    AutoH3Tool
  \    '--'    /  
   '--      --'   "I learned python to make this"
     /__/\__\                         -Mazzaferno''')


window.mainloop()  