import os

os.chdir('c:\\Users\\Andriusb\\Desktop')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)
