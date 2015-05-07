import json
import requests
import tkinter as Tkinter
from bs4 import BeautifulSoup
import urllib3
import math
import iviewdownloader
from tkinter import filedialog

class SeriesListing:
	def __init__(self, url):
		r = requests.get(url)
		self.url = url
		self.listing = json.loads(r.text)
	def getListing(self):
		seriesid = self.url.split("series=")[1]
		itemindex = 0
		for item in self.listing:
			if (item['a'] == seriesid):
				return item['f']
			itemindex = itemindex + 1
		return self.listing[0]['f']


class SeriesView:
	def __init__(self, root, url):
		self.master = root
		self.frame = Tkinter.Frame(root)
		root.geometry("{}x{}".format(800,600))
		self.entryText = Tkinter.StringVar()
		entry = Tkinter.Entry(self.frame, textvariable=self.entryText, width=200, state=Tkinter.DISABLED)
		changedirbutton = Tkinter.Button(self.frame, text="Change", command=self.changeDirectory)
		scrollbar = Tkinter.Scrollbar(self.frame, orient="vertical")
		listbox = Tkinter.Listbox(self.frame, width=800, height=600,selectmode=Tkinter.SINGLE, yscrollcommand=scrollbar.set)
		listbox.bind('<Double-Button-1>',self.callback )
		scrollbar.config(command=listbox.yview)
		listing = SeriesListing(url).getListing()
		self.listing = listing
		for item in listing:
			listbox.insert(Tkinter.END, item['b'])
		entry.pack()
		changedirbutton.pack()
		scrollbar.pack(side="right", fill="y")
		listbox.pack(side="left",fill="both", expand=True)
		self.frame.pack()

	def changeDirectory(self):
		directory = filedialog.askdirectory()
		self.entryText.set(directory)

	def callback(self,event):
		itemnumber = event.widget.curselection()[0]
		itemvalue = event.widget.get(itemnumber)
		print(self.listing[itemnumber]['a'])
		print(self.listing[itemnumber]['b'])
		print(self.listing[itemnumber]['n'])
		print(self.listing[itemnumber]['s'])
		assetid = self.listing[itemnumber]['s'].rsplit('/',1)[1][:13]
		#print(assetid)
		#self.downloadVideo(assetid)
		iviewdownloader.downloadIViewVideo(assetid, self.entryText.get() + '/' + self.listing[itemnumber]['b'] + ".mp4")


	def downloadVideo(self,assetid):
		r = requests.get('https://tviview.abc.net.au/iview/feed/sony/', verify=False);
		soup = BeautifulSoup(r.text)
		assets = soup.find_all('asset')
		for asset in assets:
			if (asset.find('id').contents[0] == assetid):
				url = asset.find('asseturl').contents[0]
				break

		#url = assets[1].find('asseturl').contents[0];
		print(url)
		request = urllib3.PoolManager().urlopen('GET', url, preload_content=False)
		with open('boo.mp4','wb') as out:
			filesize = request.getheaders()['content-length']
			blocksize = int(math.ceil(int(filesize)/100.))
			for progress in range(100):
				print("{}%".format(progress))
				out.write(request.read(blocksize))
		print("100%")
		request.release_conn()

		#print(ids[1].string)
		#print(assets[1].find('asseturl').contents[0])
		#print(r.text)


if __name__ == '__main__':
	pass
