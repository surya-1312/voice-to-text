from tkinter import *
import tkinter.messagebox
import speech_recognition as s
from googletrans import Translator

r=s.Recognizer()

root = tkinter.Tk()
root.title("...Speech__to__Text...")
root.geometry("960x540")
img=PhotoImage(file="D:\\downloads\\back.png")
frame=Label(root,image=img)
frame.place(x=0,y=0)


LANGUAGES = {
'afrikaans': 'af','albanian': 'sq','amharic': 'am', 'arabic': 'ar', 'armenian': 'hy','azerbaijani': 'az',
'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn','bosnian': 'bs','bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 
'chichewa': 'ny', 'chinese': 'zh-cn','corsican': 'co',
'croatian': 'hr', 'czech': 'cs','danish': 'da','dutch': 'nl', 'english': 'en','esperanto': 'eo','estonian': 'et',
'filipino': 'tl','finnish': 'fi', 'french': 'fr', 'frisian': 'fy','galician': 'gl','georgian': 'ka', 
'german': 'de', 'greek': 'el', 'gujarati': 'gu','haitian creole': 'ht','hausa': 'ha', 'hawaiian': 'haw', 
'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','indonesian': 'id',
'irish': 'ga','italian': 'it', 'japanese': 'ja','javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 
'khmer': 'km', 'korean': 'ko','kurdish (kurmanji)': 'ku','kyrgyz': 'ky', 'lao': 'lo','latin': 'la', 
'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb','macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn','myanmar (burmese)': 'my','nepali': 'ne', 
'norwegian': 'no', 'odia': 'or', 'pashto': 'ps','persian': 'fa', 'polish': 'pl','portuguese': 'pt','punjabi': 'pa',
'romanian': 'ro','russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr','sesotho': 'st',
'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si','slovak': 'sk','slovenian': 'sl', 'somali': 'so','spanish': 'es',
'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te','thai': 'th', 
'turkish': 'tr','ukrainian': 'uk','urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi','welsh': 'cy', 
'xhosa': 'xh','yiddish': 'yi','yoruba': 'yo','zulu': 'zu'
}

#for take input of user 
def play1():
    global lab2,lab4
    with s.Microphone() as input:
        root.update()
        audio= r.listen(input)
        root.update()         
        Text = r.recognize_google(audio)
        root.update()
        print(Text)
        
        frame=Frame(root,background="#ffcc00",height=350,width=420)
        frame.place(x=490,y=80)
        lab3=Label(frame,text="Speak the language for output ",font=("Arial",19),height=1,bg='#ffcc00')
        lab3.place(x=30,y=10)
        lab6=Label(frame,text="sentence",bg='#ffcc00',font=("Arial",16))
        lab6.place(x=20,y=70)
        lab5=Label(frame,text=Text,bg='#ffcc00',font=("Arial",20))
        lab5.place(x=20,y=100)
        lab4=Label(frame,text='',bg='#ffcc00',font=("Arial",16))
        lab4.place(x=20,y=220)
        button.config(command=lambda:translate_text(Text))
        lab2=Label(frame,text="",font=("Arial",20),height=1,bg='#ffcc00')
        lab2.place(x=20,y=250)

#for Translate the language 
def translate_text(Text):
        global LANGUAGES,lab2
        lab2['text']=""
        with s.Microphone() as input1:
                audio1= r.listen(input1)         
                lan= r.recognize_google(audio1)
                lan=lan.lower()
                lab4["text"]=lan
                if(lan in LANGUAGES.keys()):
                        lancode=LANGUAGES[lan]
                else:
                        print("language is not present in dictonary")        
                root.update()
                translator= Translator()
                root.update()
                lang2= translator.translate(Text,dest=lancode)
                lab2['text']=lang2.text


micimg=PhotoImage(file="D:\\downloads\\1232.png")
button=Button(root,image=micimg,bg='#ffde59',bd=0,command =lambda:play1())
button.place(x=190,y=120)
exitimg=PhotoImage(file="D:\\downloads\\log.png")
button2=Button(root,image=exitimg,bg="#ffcc00",bd=0,command=root.destroy)
button2.place(x=700,y=425)
root.mainloop()