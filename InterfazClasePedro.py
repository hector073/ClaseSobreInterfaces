#########################################IMPORTS######################################################

from tkinter import * #el * va a importar todo de la libreria de tkinter
from tkinter import ttk

#from tkinter import ttk #themed tk (para interfaces mas bonitas)
combobox_list =["optn1","optn2","optn3","optn4","optn5"]
#########################################FUNCIONES######################################################
def donothing():
    pass

def hello(event):
    w = event.widget
    index = int(listbox.curselection()[0])
    print(listbox.get(index))

def bye(event=None):
    print(combobox.current())
    print(combobox.get())

#########################################interfaz######################################################
root = Tk() #Toplevel widget of Tk which represents mostly the main window of an application. 
#It has an associated Tcl interpreter.

barra_menu = Menu(root)

#First sub-menu
filemenu = Menu(barra_menu, tearoff=0)
filemenu.add_command(label = "open ", command = donothing())
barra_menu.add_cascade(label = "File", menu = filemenu)

root.config(menu = barra_menu)

comandos = LabelFrame(root, text = "Comandos")
comandos.grid(row=0, column = 0, columnspan=2)

label_boton = Label(comandos, text = "tk.button")
label_boton.grid(row=0,column=0)
btn_boton = Button(comandos, text = "tk.button")
btn_boton.grid(row=0,column=1)

label_boton2 = Label(comandos, text = "tk.button2")
label_boton2.grid(row=1,column=0)
btn_boton2 = ttk.Button(comandos, text = "tk.button2")
btn_boton2.grid(row=1,column=1, padx = 10)

label_menutxt = Label(comandos, text = "menu(see examples above)")
label_menutxt.grid(row = 2, column = 0, columnspan=2)

label_espaciador = Label(comandos, text = "", width = 20)
label_espaciador.grid(row = 0 , column = 3)

choosing_frame= LabelFrame(root, text="choosing form a list", fg="blue")
choosing_frame.grid(row = 0 , column = 3)
label_tklistbox= Label(choosing_frame, text="tklistbook")
label_tklistbox.grid(row= 0,column=0)
listbox = Listbox(choosing_frame, height = 4)
listbox.grid(row=0,column=1)

for item in range(1,5):
    listbox.insert(END, "choice" + str(item))
listbox.bind('<<Listboxselect>>', hello)

label_combobox = Label(choosing_frame, text = "ttk.combobox")
label_combobox.grid(row=1,column=0)
combobox=ttk.Combobox(choosing_frame, values = combobox_list)
combobox.grid(row=1,column=1)

""" for item in range(1,5):
    listbox.insert(END, "choice" + str(item))
listbox.bind('<<Listboxselect>>', hello) """

""" 
label = Label(root, text = "hola")
label.pack()
label2 = Label(root, text = "adios", )
label2.pack()
 """


root.mainloop()

""" 
#first sub menu
filemenu = Menu(barra_menu, tearoff=0)
filemenu.add_command(label = "Open", command=donothing())
filemenu.add_command(label = "Save", command=donothing())
filemenu.add_command(label = "Exit", command=donothing())
filemenu.add_separator()
filemenu.add_command(label = "Properties", command=donothing())
barra_menu.add_cascade(label="File", menu = filemenu)

#second sub menu
editmenu = Menu(barra_menu, tearoff=0)
editmenu.add_command(label = "Open", command=donothing())
editmenu.add_command(label = "Save", command=donothing())
editmenu.add_command(label = "Exit", command=donothing())
editmenu.add_separator()
editmenu.add_command(label = "Properties", command=donothing())
barra_menu.add_cascade(label="edit", menu = editmenu)

'''
barra_menu.add_command(label="file", command=donothing())
barra_menu.add_command(label="edith", command=donothing())
barra_menu.add_command(label="help", command=donothing())
'''

open_bth = Menubutton()

root.config( menu= barra_menu)


root.mainloop()#corre a la interfaz en un ciclo

 """
