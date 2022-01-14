from urllib.request import urlretrieve
import os
def download(url, cot, ver, filename):
    print(url + " => " + str(filename))
    try:
        os.mkdir("./" + cot.title() + "-" + ver)
    except FileExistsError:
        pass
    urlretrieve(url, "./" + cot.title() + "-" + ver + "/" + str(filename))
    return True
