from get_probabilities import get_propability_of_all_words
import pickle

with open("./tokenizer_output/lower_sentences", "rb") as fp:
  sentences = pickle.load(fp)
  
with open("./ngram_counter_output/bigrams", "rb") as fp:
  bigrams = pickle.load(fp)
  
with open("./ngram_counter_output/trigrams", "rb") as fp:
  trigrams = pickle.load(fp)

with open("./vocabulary_output/vocabulary", "rb") as fp:
  vocab = pickle.load(fp)
    

# print(get_propability_of_all_words(["how", "do"], bigrams, trigrams, vocab, k=1))


from tkinter import *
import tkinter.font
from PIL import Image,ImageTk


    
def get_input():
   value=text_box.get("1.0",'end-1c').split(' ')
   propabilities = get_propability_of_all_words([value[-2], value[-1]], bigrams, trigrams, vocab, k=1)
   if len(text_box2.get("1.0", END))!=1:
       text_box2.delete("1.0","end")
   text_box2.insert(END, str(propabilities).replace("{","").replace('}','').replace(',','\n').replace('\'',""))
   if len(text_box3.get("1.0", END))!=1:
       text_box3.delete("1.0","end")
   text_box3.insert(END, str(list(propabilities.keys())[:3]).replace("[","").replace(']','').replace(',','\n').replace('\'',""))
   

window=Tk()
window.title('selected 3 project')
window.geometry('1000x500+20+50')
window.maxsize(width=1366,height=768)
img=Image.open('./background.jpg')
bg=ImageTk.PhotoImage(img)
label=Label(window,image=bg).place(x=0,y=0)
label1=Label(window,text='Auto-complete',bg='lightcyan',fg='black' ,font="Times 15 italic bold").place(x=300,y=10)
text_box=Text(window,height=15,width=100,bg='lightcyan',font="Times 12  bold")
text_box.place(x=300,y=50)
text_box2=Text(window,height=12,width=65,bg='lightblue',font="Times 12  bold", wrap = WORD)
text_box2.place(x=50,y=470)
text_box3=Text(window,height=12,width=65,bg='lightblue',font="Times 12  bold", wrap = WORD)
text_box3.place(x=800,y=470)
comment= Button(window, height=2, width=10, text="Complete", command=get_input).place(x=400,y=350)
window.mainloop()

