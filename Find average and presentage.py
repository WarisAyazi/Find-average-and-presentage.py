"""
This program Designed by Abdul waris Ayazi
Data: Mon, 27 Nev, 2023
"""


import customtkinter , tkinter
from  tkinter import IntVar
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = tkinter.Tk()
root.geometry("800x540")
root.resizable(False,False)
root.title("Find average and presentage")
tab = customtkinter.CTkTabview(root,height=500,width= 700,)
tab.pack(padx= 10, pady = 10)

tab.add("Information System",)
tab.add("Information technology")
tab.add("Software Engineering")

tab.set("Information System")

# Information System
def reset ():
        python.delete(0, END)
        math.delete(0, END) 
        CS.delete(0, END) 
        Serat.delete(0, END) 
        Saqifat.delete(0, END)  
        English.delete(0, END)
        
pythonV = IntVar()
mathV = IntVar()
CSV = IntVar()
SaqifatV = IntVar()
SeratV = IntVar()
EnglishV = IntVar()

aver = IntVar()
percen = IntVar()

def fine ():
    ave = (pythonV.get() + mathV.get() + CSV.get() + SaqifatV.get() + SeratV.get() + EnglishV.get()) / 6
    aver.set(ave)

    per = ((pythonV.get() * 4) + (mathV.get() * 4)  + 
           (CSV.get()* 4)  + (SaqifatV.get() * 2)  + 
           (SeratV.get()* 2)  + (EnglishV.get()* 2) ) / 18
    percen.set(per)

    presentage1 = customtkinter.CTkLabel(tab.tab("Information System"), text="Your Persentage is :",font=("Arial",20, "bold", ))
    presentage1.place(x =150,y= 300)
    presentage2 = customtkinter.CTkLabel(tab.tab("Information System"), textvariable= percen,font=("Arial",20, "bold", ))
    presentage2.place(x =400,y= 300)

    average1 = customtkinter.CTkLabel(tab.tab("Information System"), text="Your Average:",font=("Arial",20, "bold", ))
    average1.place(x =150,y= 340)
    average2 = customtkinter.CTkLabel(tab.tab("Information System"), textvariable = aver,font=("Arial",20, "bold", ))
    average2.place(x =400,y= 340)


python = customtkinter.CTkLabel(tab.tab("Information System"), text="Python:",font=("Arial",20, "bold", ))
python.place(x =150,y= 20)
python = customtkinter.CTkEntry(tab.tab("Information System"),textvariable=pythonV)
python.place(x =400,y= 20)

math = customtkinter.CTkLabel(tab.tab("Information System"), text="Discrete mathematics:",font=("Arial",20, "bold", ))
math.place(x =150,y= 60)
math = customtkinter.CTkEntry(tab.tab("Information System"),textvariable=mathV)
math.place(x =400,y= 60)

CS = customtkinter.CTkLabel(tab.tab("Information System"), text="CS Fundamentals:",font=("Arial",20, "bold", ))
CS.place(x =150,y= 100)
CS = customtkinter.CTkEntry(tab.tab("Information System"),textvariable=CSV)
CS.place(x =400,y= 100)

English = customtkinter.CTkLabel(tab.tab("Information System"), text="English:",font=("Arial",20, "bold", ))
English.place(x =150,y= 140)
English = customtkinter.CTkEntry(tab.tab("Information System"),textvariable=EnglishV)
English.place(x =400,y= 140)

Saqifat = customtkinter.CTkLabel(tab.tab("Information System"), text="Saqifat Islami",font=("Arial",20, "bold", ))
Saqifat.place(x =150,y= 180)
Saqifat = customtkinter.CTkEntry(tab.tab("Information System"),textvariable=SaqifatV)
Saqifat.place(x =400,y= 180)

Serat = customtkinter.CTkLabel(tab.tab("Information System"), text="Serat:",font=("Arial",20, "bold", ))
Serat.place(x =150,y= 220)
Serat = customtkinter.CTkEntry(tab.tab("Information System"),textvariable=SeratV)
Serat.place(x =400,y= 220)


fine_But = customtkinter.CTkButton(tab.tab("Information System"), text= "Fine", font=("Arial",20, "bold",),command=fine)
fine_But.place(x = 400, y = 260)

reset_But = customtkinter.CTkButton(tab.tab("Information System"), text= "Reset", font=("Arial",20, "bold",),command=reset)
reset_But.place(x = 150, y = 260)

Ayazi = customtkinter.CTkLabel(tab.tab("Information System"), text="Designer Abdul Waris Ayazi ",font=("Chilanka",24, "bold", ))
Ayazi.place(x =180,y= 420)
# Information technology
def resetT ():
        Tpython.delete(0, END)
        Tmath.delete(0, END) 
        TCS.delete(0, END) 
        TSerat.delete(0, END) 
        TSaqifat.delete(0, END)  
        TEnglish.delete(0, END)
        TAlgebra.delete(0, END)
        

pythonT = IntVar()
mathT = IntVar()
CST = IntVar()
SaqifatT = IntVar()
SeratT = IntVar()
EnglishT = IntVar()
linear = IntVar()

averT = IntVar()
percenT = IntVar()
def fineT ():
    ave = (pythonT.get() + mathT.get() + CST.get() + SaqifatT.get() +
            SeratT.get() + EnglishT.get() + linear.get()) / 7
    averT.set(ave)

    per = ((pythonT.get() * 4) + (mathT.get() * 4)  + 
           (CST.get()* 4)  + (SaqifatT.get() * 2)  + 
           (SeratT.get()* 2)  + (EnglishT.get()* 2) + (linear.get()* 3) ) / 21
    percenT.set(per)

    presentage1 = customtkinter.CTkLabel(tab.tab("Information technology"), text="Your Persentage is :",font=("Arial",20, "bold", ))
    presentage1.place(x =150,y= 340)
    presentage2 = customtkinter.CTkLabel(tab.tab("Information technology"), textvariable= percenT,font=("Arial",20, "bold", ))
    presentage2.place(x =400,y= 340)

    average1 = customtkinter.CTkLabel(tab.tab("Information technology"), text="Your Average:",font=("Arial",20, "bold", ))
    average1.place(x =150,y= 380)
    average2 = customtkinter.CTkLabel(tab.tab("Information technology"), textvariable = averT,font=("Arial",20, "bold", ))
    average2.place(x =400,y= 380)

Tpython = customtkinter.CTkLabel(tab.tab("Information technology"), text="Python:",font=("Arial",20, "bold", ))
Tpython.place(x =150,y= 20)
Tpython = customtkinter.CTkEntry(tab.tab("Information technology"), textvariable=pythonT)
Tpython.place(x =400,y= 20)

Tmath = customtkinter.CTkLabel(tab.tab("Information technology"), text="Discrete mathematics:",font=("Arial",20, "bold", ))
Tmath.place(x =150,y= 60)
Tmath = customtkinter.CTkEntry(tab.tab("Information technology"), textvariable=mathT)
Tmath.place(x =400,y= 60)

TCS = customtkinter.CTkLabel(tab.tab("Information technology"), text="CS Fundamentals:",font=("Arial",20, "bold", ))
TCS.place(x =150,y= 100)
TCS = customtkinter.CTkEntry(tab.tab("Information technology"), textvariable=CST)
TCS.place(x =400,y= 100)

TEnglish = customtkinter.CTkLabel(tab.tab("Information technology"), text="English:",font=("Arial",20, "bold", ))
TEnglish.place(x =150,y= 140)
TEnglish = customtkinter.CTkEntry(tab.tab("Information technology"), textvariable=EnglishT)
TEnglish.place(x =400,y= 140)

TSaqifat = customtkinter.CTkLabel(tab.tab("Information technology"), text="Saqifat Islami",font=("Arial",20, "bold", ))
TSaqifat.place(x =150,y= 180)
TSaqifat = customtkinter.CTkEntry(tab.tab("Information technology"), textvariable= SaqifatT)
TSaqifat.place(x =400,y= 180)

TSerat = customtkinter.CTkLabel(tab.tab("Information technology"), text="Serat:",font=("Arial",20, "bold", ))
TSerat.place(x =150,y= 220)
TSerat = customtkinter.CTkEntry(tab.tab("Information technology"), textvariable=SeratT)
TSerat.place(x =400,y= 220)

TAlgebra = customtkinter.CTkLabel(tab.tab("Information technology"), text="Linear Algebra:",font=("Arial",20, "bold", ))
TAlgebra.place(x =150,y= 260)
TAlgebra = customtkinter.CTkEntry(tab.tab("Information technology"), textvariable=linear)
TAlgebra.place(x =400,y= 260)

Tfine_But = customtkinter.CTkButton(tab.tab("Information technology"), text= "Fine", font=("Arial",20, "bold",),command=fineT)
Tfine_But.place(x = 400, y = 300)

Treset_But = customtkinter.CTkButton(tab.tab("Information technology"), text= "Reset", font=("Arial",20, "bold",),command=resetT)
Treset_But.place(x = 150, y = 300)

TAyazi = customtkinter.CTkLabel(tab.tab("Information technology"), text="Designer Abdul Waris Ayazi ",font=("Chilanka",24, "bold", ))
TAyazi.place(x =180,y= 420)
# Software Engineering
def resetS ():
        Spython.delete(0, END)
        Smath.delete(0, END) 
        SSerat.delete(0, END) 
        SSaqifat.delete(0, END)  
        SEnglish.delete(0, END)
        SDatabase.delete(0, END)
        SDLD.delete(0, END) 

pythonS = IntVar()
mathS = IntVar()
DatabaseS = IntVar()
SaqifatS = IntVar()
SeratS = IntVar()
EnglishS = IntVar()
DLDS = IntVar()

averS = IntVar()
percenS = IntVar()
 
def fineS ():
    ave = (pythonS.get() + mathS.get() + DatabaseS.get() + SaqifatS.get() +
            SeratS.get() + EnglishS.get() + DLDS.get()) / 7
    averS.set(ave)

    per = ((pythonS.get() * 4) + (mathS.get() * 4)  + 
           (DatabaseS.get()* 4)  + (SaqifatS.get() * 2)  + 
           (SeratS.get()* 2)  + (EnglishS.get()* 2) + (DLDS.get()* 4) ) / 22
    percenS.set(per)

    presentage1 = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Your Persentage is :",font=("Arial",20, "bold", ))
    presentage1.place(x =150,y= 340)
    presentage2 = customtkinter.CTkLabel(tab.tab("Software Engineering"), textvariable= percenS,font=("Arial",20, "bold", ))
    presentage2.place(x =400,y= 340)

    average1 = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Your Average:",font=("Arial",20, "bold", ))
    average1.place(x =150,y= 380)
    average2 = customtkinter.CTkLabel(tab.tab("Software Engineering"), textvariable = averS,font=("Arial",20, "bold", ))
    average2.place(x =400,y= 380)

Spython = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Python:",font=("Arial",20, "bold", ))
Spython.place(x =150,y= 20)
Spython = customtkinter.CTkEntry(tab.tab("Software Engineering"), textvariable=pythonS)
Spython.place(x =400,y= 20)

Smath = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Discrete mathematics:",font=("Arial",20, "bold", ))
Smath.place(x =150,y= 60)
Smath = customtkinter.CTkEntry(tab.tab("Software Engineering"), textvariable=mathS)
Smath.place(x =400,y= 60)

SDatabase = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Database Concepts:",font=("Arial",20, "bold", ))
SDatabase.place(x =150,y= 100)
SDatabase = customtkinter.CTkEntry(tab.tab("Software Engineering"), textvariable=DatabaseS)
SDatabase.place(x =400,y= 100)

SEnglish = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="English:",font=("Arial",20, "bold", ))
SEnglish.place(x =150,y= 140)
SEnglish = customtkinter.CTkEntry(tab.tab("Software Engineering"), textvariable=EnglishS)
SEnglish.place(x =400,y= 140)

SSaqifat = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Saqifat Islami",font=("Arial",20, "bold", ))
SSaqifat.place(x =150,y= 180)
SSaqifat = customtkinter.CTkEntry(tab.tab("Software Engineering"), textvariable=SaqifatS)
SSaqifat.place(x =400,y= 180)

SSerat = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Serat:",font=("Arial",20, "bold", ))
SSerat.place(x =150,y= 220)
SSerat = customtkinter.CTkEntry(tab.tab("Software Engineering"), textvariable=SeratS)
SSerat.place(x =400,y= 220)

SDLD = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="DLD:",font=("Arial",20, "bold", ))
SDLD.place(x =150,y= 260)
SDLD = customtkinter.CTkEntry(tab.tab("Software Engineering"), textvariable=DLDS)
SDLD.place(x =400,y= 260)

Sfine_But = customtkinter.CTkButton(tab.tab("Software Engineering"), text= "Fine", font=("Arial",20, "bold",),command=fineS)
Sfine_But.place(x = 400, y = 300)

Sreset_But = customtkinter.CTkButton(tab.tab("Software Engineering"), text= "Reset", font=("Arial",20, "bold",),command=resetS)
Sreset_But.place(x = 150, y = 300)

SAyazi = customtkinter.CTkLabel(tab.tab("Software Engineering"), text="Designer Abdul Waris Ayazi",font=("Chilanka",24, "bold", ))
SAyazi.place(x =180,y= 420)


root.mainloop()