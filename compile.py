import os

count = 2
while True:
    try:
        import PyInstaller
        import win32api
        print("Building pbrain-jellyfish...")
        os.system("pyinstaller pbrain.py pisqpipe.py --name pbrain-jellyfish.exe --onefile")
        break
    except:
        print("pywin32 or PyInstaller does not exist, now trying to install them...")
        os.system("pip3 install pypiwin32")
        os.system("pip3 install pyinstaller")
        count -= 1
        continue
