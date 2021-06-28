from urllib.request import urlretrieve
import os
def download(url, cot, ver, filename):
    print(url + " => " + str(filename))
    try:
        os.mkdir("/disk/CTD/" + cot.title() + "-" + ver)
    except FileExistsError:
        pass
    urlretrieve(url, "/disk/CTD/" + cot.title() + "-" + ver + "/" + str(filename))
    return True
