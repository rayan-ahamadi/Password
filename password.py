from tkinter import *
from tkinter import messagebox
from hashlib import *
import json

def verifieMdp(chaine): 
    global mdpChiffré
    if len(chaine) < 8 : 
        messagebox.showerror("Erreur","Votre mdp doit avoir au moins 8 caractères")
        return 0
    majuscule = False
    for i in chaine :
        if ord(i) > 64 and ord(i) < 91 :
            majuscule = True 
            break
    if majuscule == False :
        messagebox.showerror("Erreur","Votre mdp doit avoir une majuscule")
        return 0

    minuscule = False
    for i in chaine :
        if ord(i) > 96 and ord(i) < 123 :
            minuscule = True 
            break
    if minuscule == False :
        messagebox.showerror("Erreur","Votre mdp doit avoir une minuscule")
        return 0

    chiffre = False
    for i in chaine :
        if ord(i) > 47 and ord(i) < 58 :
            chiffre = True 
            break
    if chiffre == False :
        messagebox.showerror("Erreur","Votre mdp doit contenir un chiffre ")
        return 0

    AsciiSpéciaux = [ord("!"),ord("@"),ord("#"),ord("$"),ord("%"),ord("^"),ord("&"),ord("*") ]
    charSpéciaux = False 
    for i in chaine:
        if ord(i) in AsciiSpéciaux:
            charSpéciaux = True
            break
    if charSpéciaux == False : 
        messagebox.showerror("Erreur","Votre mdp doit contenir un caractère spécial")
        return 0

    messagebox.showinfo("MDP valide", "Votre mot de passe est assez fort pour utilisation")
    mdpChiffré.delete(0,END)
    encode = str(chaine).encode()
    Sha = sha256(encode).hexdigest()
    mdpChiffré.insert(0,Sha)

    mdpDict = {
        "mdp" : chaine,
        "crypted" : Sha
    }

    with open('mdp.json', 'w') as mon_fichier:
	    json.dump(mdpDict, mon_fichier)
    

window = Tk()
window.title("Vérificateur de Mot de Passe")
window.geometry("400x300")

frame = Frame(window)
Label(frame,text="Tapez un mot de passe",font=("Arial",20)).grid(row=0,column=0,pady=10)
mdp = Entry(frame,show="*")
valider = Button(frame,text="Vérification",command= lambda : verifieMdp(mdp.get()))
Label(frame,text="Mot de passe chiffré : ").grid(row=4,column=0,pady=5)
mdpChiffré = Entry(frame,width=50)


frame.grid(row=1,column=0,pady=50,padx=50)
mdp.grid(row=1,column=0)
valider.grid(row=2,column=0,pady=10)
mdpChiffré.grid(row=5,column=0,pady=10)


window.mainloop()