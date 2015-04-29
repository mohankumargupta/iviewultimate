import json
import requests

class Listing():
	def __init__(self):
		r = requests.get('http://iview.abc.net.au/api/legacy/flash/?seriesIndex')
		self.listing = json.loads(r.text);
	def getListing(self):
		return self.listing


if __name__ == '__main__':
	listing = Listing()
	print(len(listing.getListing()))
	print(listing.getListing()[0])
	print(listing.getListing()[0]['b'])

