import json 
import requests 
tgrepo = "https://api.github.com/repos/telegramdesktop/tdesktop/releases/latest" 
rawdata = requests.get(tgrepo) 
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


