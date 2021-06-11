from tkinter import *
from tkinter.ttk import Progressbar
import requests
from bs4 import BeautifulSoup
import time
import os
from PIL import Image, ImageDraw, ImageFont
import pyautogui
import time
import webbrowser
import facebook

#functions



def fbAutomation():

    try:
        if caption.get() =="":
            cap="#covid19livedata #coronavirus #corona #nepalcorona"

        else:
            cap=caption.get()

        page_access_token = "EAAHIOphs84kBAG6aAKSZAkNiVSJ5ndiyQzFs7XQJF9acvIkdgpgSvBJH7O7X7TE6NRla7zAwPiwIbSOhefP7pdXIm24ETlY6z2FgNWX7vtchEpDkZCOmHr1btCgqh0MAMZAdEjH95lOkFlBXSxRgsKfaKnq7MZAkxl2FEXy5QKZB4kOEnkiaj"
        graph = facebook.GraphAPI(page_access_token)
        facebook_page_id = "1542296019147773"
        # graph.put_object(facebook_page_id, "feed",message="corona update 1 ")
        graph.put_photo(open("coronaimg.jpg", "rb"), message=cap)

    except:
        print("if there is no internet connection \n OR contact us on 'ajayoneness123@gmail.com'")

def imgCreate(data):
    img = Image.open("sample_in.jpg")
    # img = Image.new('RGB', (500, 300), color=(73, 10, 15))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("sans-serif.ttf", 70)

    d.text((20, 70), data, fill=(255, 255, 255), font=font)
    img.save("coronaimg.jpg")

def maindata(country):
    i=1
    while (i<=1):
        try:
            livedata = f"COVID19 LIVE DATA({country})"
            url = f"https://www.worldometers.info/coronavirus/country/{country}"
            req = requests.get(url)
            bsobj = BeautifulSoup(req.text, 'html.parser')
            data = bsobj.find_all('div', class_="maincounter-number")
            ttime = time.ctime()
            cases = data[0].text.strip()
            tcase = f"Total Cases : {cases[0:]}"

            death = data[1].text.strip()
            tdeath = f"Total Deaths : {death[0:]}"

            recovered = data[2].text.strip()
            trecovered = f"Total Recovered : {recovered[0:]}"

            data = f"       {livedata}\n\n     {ttime}\n\n{tcase}\n{tdeath}\n{trecovered}"
            #d = f"{str(livedata)}\n{str(ttime)}\n{str(tcase)}\n{str(tdeath)}\n{str(trecovered)}"
            imgCreate(data)
            #fbAutomation()
            #time.sleep(3600)
            i=i+1
        except:
            print("No internet connection")
            i=i+1

def imgctd():
    ic = "image created"
    dc.config(text=ic)


def fbatm():
    fbb="Posted on your fb page Hacking knowledge "
    dc1.config(text=fbb)

def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    colldata="Collecting data"
    cdata.config(text=colldata)
    time.sleep(1)

    progress['value'] = 30
    root.update_idletasks()
    livedata = "COVID19 LIVE DATA"
    space.config(text=livedata)
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    country=["nepal","india","china"]

    maindata(country[2])
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    imgctd()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    post="posting........"
    pos.config(text=post)
    time.sleep(1)

    progress['value'] = 90
    root.update_idletasks()
    fbAutomation()
    time.sleep(1)

    progress['value'] = 100
    root.update_idletasks()
    fbatm()
    time.sleep(1)







root=Tk()
root.geometry("500x500")
root.title("COVID19 updateer")
bgcol="black"
fgcol="white"
mfnt="arial 15 bold"
lfnt="arial 20 bold"
sfnt="arial 10 bold"

root.config(background=bgcol)

welcometext=Label(root,text="welcome to \nauto FB post COVID19 update",bg=bgcol,fg=fgcol,font=lfnt)
captionTitle=Label(root,text="write caption",bg=bgcol,fg=fgcol,font=mfnt)
caption=Entry(root,bg=bgcol,fg=fgcol,font=lfnt)
cdata=Label(root,bg=bgcol,fg=fgcol,font=sfnt)
space=Label(root,bg=bgcol)

dc=Label(root,bg=bgcol,fg=fgcol,font=sfnt)
pos=Label(root,bg=bgcol,fg=fgcol,font=sfnt)
dc1=Label(root,bg=bgcol,fg=fgcol,font=sfnt)


progress = Progressbar(root, orient=HORIZONTAL,length=400, mode='determinate')
start=Button(root,text = "START",bg=bgcol,fg=fgcol,font=lfnt,command=bar)

#packing...
welcometext.pack()
captionTitle.pack()
caption.pack()
cdata.pack()
space.pack()
dc.pack()
pos.pack()
dc1.pack()
progress.pack(pady=10)
start.pack()


root.mainloop()