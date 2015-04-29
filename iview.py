import sys
import tkinter as Tkinter
from listing import Listing

def callback(event):
	#print(dir(event))
	itemnumber = event.widget.curselection()[0]
	itemvalue = event.widget.get(itemnumber)
	print(itemvalue)


root = Tkinter.Tk()
root.geometry("{}x{}".format(800,600))

scrollbar = Tkinter.Scrollbar(root, orient="vertical")

#print(dir(root))
#l = Tkinter.Label(root, text="Hello, world!\nTkinter on PocketPC!\nSee http://pythonce.sf.net.")
#b = Tkinter.Button(root, text='Quit', command=root.destroy)
#e = Tkinter.Entry(root)
listbox = Tkinter.Listbox(root, width=800, height=600,selectmode=Tkinter.SINGLE, yscrollcommand=scrollbar.set)
listbox.bind('<Double-Button-1>',callback )
scrollbar.config(command=listbox.yview)
listing = Listing().getListing()

#print(dir(listbox))
#print(len(listing))
i=0
for item in listing:
	listbox.insert(Tkinter.END, item['b'])
	i = i + 1

scrollbar.pack(side="right", fill="y")
listbox.pack(side="left",fill="both", expand=True)
#l.pack()
#b.pack()
root.mainloop()