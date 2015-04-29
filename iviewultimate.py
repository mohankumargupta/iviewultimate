import tkinter as Tkinter
from listing import ListingView

root = Tkinter.Tk()
ListingView(root, 'http://iview.abc.net.au/api/legacy/flash/?seriesIndex')
root.mainloop()