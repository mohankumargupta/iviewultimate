import requests
from bs4 import BeautifulSoup
from time import sleep
import threading
import urllib3
import math

def run_in_thread(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

@run_in_thread
def downloadIViewVideo(assetid, downloadurl):
    while not IViewDownloader.soup :
        print("sleeping for 10 seconds")
        sleep(10)

    assets = IViewDownloader.soup.find_all('asset')

    for asset in assets:
        if (asset.find('id').contents[0] == assetid):
            url = asset.find('asseturl').contents[0]
            break

    request = urllib3.PoolManager().urlopen('GET', url, preload_content=False)
    with open(downloadurl,'wb') as out:
        filesize = request.getheaders()['content-length']
        blocksize = int(math.ceil(int(filesize)/100.))

        for progress in range(100):
            print("{}%".format(progress))
            out.write(request.read(blocksize))

    print("100%")
    request.release_conn()

class IViewDownloader:
    IVIEWFEED = 'https://tviview.abc.net.au/iview/feed/sony/'
    isDownloaded = False
    soup = None;

    def __init__(self):
        pass

    @run_in_thread
    def download(self):
        r = requests.get(IViewDownloader.IVIEWFEED, verify=False);
        IViewDownloader.soup = BeautifulSoup(r.text)
        IViewDownloader.isDownloaded = True;
        print('It has been downloaded')
