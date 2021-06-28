from urllib.request import urlretrieve
import os
def download(url, cot, ver, filename):
    print(url + " => " + str(filename))
    os.mkdir("/disk/CTD/" + cot.title() + "-" + ver)
    urlretrieve(url, "/disk/CTD/" + cot.title() + "-" + ver + "/" + str(filename))
    return True
