from tkinter import *
from gng import *

def humanvspc():
    menu_principal.destroy()
    def play():
        a = int(number.get())
        res = game.play(a)
        texto = StringVar()
        texto.set(res)      
        color = 'black'
        if res == 'You win':
            color = 'green'
        answer = Entry(menu,textvariable=texto,fg= color).place(x=100,y=60)

    menu = Tk()
    menu.geometry('380x150')
    game = HumanAgainstComputerGame()    
    menu.title('PLAYER VS PC')
    label1 = Label(menu,text = 'Yo pienso un numero,tu tienes que adivinarlo!',font=('',10))
    label1.grid(row=2,column=1)
    label2 = Label(menu,text='Numero del 0 al 100>>').place(x=10,y=30)
    number = StringVar()
    number.set('0')
    box = Entry(menu,width=10,textvariable=number).place(x=180,y=30)
    boton_enter = Button(menu,text='Enter',command = play).place(x=300,y=25)
    salir = Button(menu,text='Salir',font = ('',10),fg ='red',command = quit).place(x=100,y=95)  
    menu.mainloop()

def pcvshuman():
    menu = Tk()
    menu.title('PC VS PLAYER')
    menu.mainloop()

#Manu principal
menu_principal = Tk()
menu_principal.title('GAME OF 100')
label1 = Label(menu_principal,text='Quien contra quien?',font=('',15))
label1.grid(row=1,column=2)
boton1 = Button(menu_principal,text = 'Player >contra> PC',command = humanvspc)
boton1.grid(row=2,column=1)
boton2 = Button(menu_principal,text = 'PC >contra> Player',command = pcvshuman)
boton2.grid(row=2,column=3)
boton3 = Button(menu_principal,text = 'Quit',fg = 'red',command = quit)
boton3.grid(row = 4,column = 2)
menu_principal.mainloop()