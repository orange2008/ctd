import json 
import requests 
import download as dl
print("Requesting for Github API")
tgrepo = "https://api.github.com/repos/telegramdesktop/tdesktop/releases/latest" 
rawdata = requests.get(tgrepo) 
print("Status code: " + str(rawdata.status_code))
print("Parsing API callback..")
rawjson = rawdata.json() 
for i in range(0,7): 
    label = rawjson["assets"][i]["label"] 
    if "Windows 32 bit: Installer" in label:
        setup_win32 = [rawjson["assets"][i]["browser_download_url"], rawjson["assets"][i]["name"]] 
        setup_win32[1] = setup_win32[1].replace("tsetup", "Telegram.Windows.i386") 
    elif "Windows 64 bit: Installer" in label: 
        setup_win64  = [rawjson["assets"][i]["browser_download_url"], rawjson["assets"][i]["name"]]  
        setup_win64[1] = setup_win64[1].replace("tsetup-x64", "Telegram.Windows.amd64") 
    elif "Windows 32 bit: Portable" in label: 
        portable_win32 = [rawjson["assets"][i]["browser_download_url"], rawjson["assets"][i]["name"]] 
        portable_win32[1] = portable_win32[1].replace("tportable", "Telegram.Windows.i386.Portable") 
    elif "Windows 64 bit: Portable" in label: 
        portable_win64 = [rawjson["assets"][i]["browser_download_url"], rawjson["assets"][i]["name"]] 
        portable_win64[1] = portable_win64[1].replace("tportable-x64", "Telegram.Windows.amd64.Portable") 
    elif "macOS" in label: 
        macos  = [rawjson["assets"][i]["browser_download_url"], rawjson["assets"][i]["name"]] 
        macos[1] = macos[1].replace("tsetup", "Telegram.macOS") 
    elif "Linux" in label: 
        linux  = [rawjson["assets"][i]["browser_download_url"], rawjson["assets"][i]["name"]] 
        linux[1] = linux[1].replace("tsetup", "Telegram.Linux") 
    elif "Source" in label: 
        src = [rawjson["assets"][i]["browser_download_url"], rawjson["assets"][i]["name"]] 
        src[1] = src[1].replace("tdesktop", "Telegram.Desktop.Source.Code") 
    else:
        print("Invalid API feedback.")

version = rawjson["tag_name"]
print("Parsed.")
print("Downloading files...")
dl.download(setup_win32[0], "Telegram", version, setup_win32[1])
dl.download(setup_win64[0], "Telegram", version, setup_win64[1])
dl.download(portable_win32[0], "Telegram", version, portable_win32[1])
dl.download(portable_win64[0], "Telegram", version, portable_win64[1])
dl.download(macos[0], "Telegram", version, macos[1])
dl.download(linux[0], "Telegram", version, linux[1])
dl.download(src[0], "Telegram", version, src[1])
dl.download("https://telegram.org/dl/android/apk", "Telegram", "mobile", "Telegram.apk")
print("File downloaded.")
print("Copyright 2021 Frank Ruan(CEO). ORWTMC Corporation reserved all the rights.")
