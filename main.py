import sys
import requests
import tkinter

ARGS = sys.argv

req = requests.get(ARGS[1])

while req.status_code != int(ARGS[2]):
    print('Error. Requesting again...')
    req = requests.get(ARGS[1])

window = tkinter.Tk()
window.title('site request checker')
window.geometry('300x200')

label = tkinter.Label(text="Site is correcctly responding")
label.pack()

window.mainloop()

print('End')
