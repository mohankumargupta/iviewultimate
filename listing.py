import json
import requests
import tkinter as Tkinter
from series import SeriesView
import iviewdownloader

class Listing:
	def __init__(self, url):
		r = requests.get(url)
		self.listing = json.loads(r.text);
	def getListing(self):
		return self.listing


class ListingView:
	def __init__(self, root, url):
		self.master = root
		self.frame = Tkinter.Frame(root)
		root.geometry("{}x{}".format(800,600))
		scrollbar = Tkinter.Scrollbar(self.frame, orient="vertical")
		listbox = Tkinter.Listbox(self.frame, width=800, height=600,selectmode=Tkinter.SINGLE, yscrollcommand=scrollbar.set)
		listbox.bind('<Double-Button-1>',self.callback )
		scrollbar.config(command=listbox.yview)
		listing = Listing(url).getListing()
		self.listing = listing
		for item in listing:
			listbox.insert(Tkinter.END, item['b'])
		scrollbar.pack(side="right", fill="y")
		listbox.pack(side="left",fill="both", expand=True)
		self.frame.pack()
		downloader = iviewdownloader.IViewDownloader()
		downloader.download()

	def callback(self,event):
		itemnumber = event.widget.curselection()[0]
		itemvalue = event.widget.get(itemnumber)
		self.newWindow = Tkinter.Toplevel(self.master)
		#print(self.listing[itemnumber]['a'])
		newurl = 'http://iview.abc.net.au/api/legacy/flash/?series={}'.format(self.listing[itemnumber]['a'])
		#print(newurl)
		SeriesView(self.newWindow, newurl)
		#print(itemvalue)

if __name__ == '__main__':
	listing = Listing()
	print(len(listing.getListing()))
	print(listing.getListing()[0])
	print(listing.getListing()[0]['b'])
