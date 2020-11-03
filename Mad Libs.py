from pathlib import Path
import tkinter as tkt
from tkinter import messagebox, simpledialog
# this program open a file and lets the user change the text that can be found in the specific places of teh file, and then saves it ith another name
#TO DO: look for the file
actual_cwd = Path.cwd()

#TO DO: open the file
text_file = open(actual_cwd / 'Mad_Libs.txt')

#TO DO: read the file into a list
texto = text_file.read()

#TO DO: find the different expresions
texto_sep = texto.split()
print(texto_sep)
elementos_adj = []
elementos_noun = []
elementos_verb = []
for i, j in enumerate(texto_sep):
    if j == 'ADJECTIVE':
        elementos_adj.append(i)
    if j == 'NOUN':
        elementos_noun.append(i)
    if j == 'VERB.':
        elementos_verb.append(i)
print(elementos_adj)
print(elementos_noun)
print(elementos_verb)

#TO DO: show the user the different places to fill and let only text be written
application_window = tkt.Tk()
messagebox.showinfo("Mad Libs", "The text to change is: \n" + texto)

for i in elementos_adj:
    texto_sep[i] = simpledialog.askstring("ADJECTIVE", "What you want %s Adjective to be?"%i, parent = application_window)
for i in elementos_noun:
    texto_sep[i] = simpledialog.askstring("NOUN", "What you want %s Noun to be?"%i, parent = application_window)
for i in elementos_verb:
    texto_sep[i] = simpledialog.askstring("VERB", "What you want %s Verb to be?"%i, parent = application_window)
#TO DO: print the resultant text
texto = ' '.join(texto_sep)
messagebox.showinfo("Mad Libs", "The text to now is: \n" + texto)

#TO DO: ask the user if he/she wants to make changes, and where
answer = messagebox.askyesno("Question","Do you like to make changes?")
if answer:
    for i in elementos_adj:
        texto_sep[i] = simpledialog.askstring("ADJECTIVE", "What you want %s Adjective to be?" % i,parent=application_window)
    for i in elementos_noun:
        texto_sep[i] = simpledialog.askstring("NOUN", "What you want %s Noun to be?" % i, parent=application_window)
    for i in elementos_verb:
        texto_sep[i] = simpledialog.askstring("VERB", "What you want %s Verb to be?" % i, parent=application_window)

#TO DO: print again after changes
texto = ' '.join(texto_sep)
messagebox.showinfo("Mad Libs", "The final text is: \n" + texto)
#TO DO: ask for the name of the file to save
file_name = simpledialog.askstring("File Nmae", "What name you want to save the file as?", parent = application_window)
#TO DO: save the file
file = open(file_name + '.txt', 'w')
file.write(texto)
file.close()