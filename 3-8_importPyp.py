# Adam Lancaster
# this program displays and manipulates the contents of the clipboard.

import pyperclip as pc

def main():
# main function loads the clipboard with a message, then prints the contents
# of the clipboard. it then repeats this process with a second message. 

    clipboardPnP('this is the first message.')
    clipboardPnP('this is the second message.')

def clipboardPnP(statement):
# clipboard paste and print. I couldnt think of something better to call
# it, and clipboardPasteAndPrint is way too long. function loads statement 
# into clipboard then prints the contents of the clipboard.

    pc.copy(statement)
    # this function copies the msg txt to clipboard.
    
    print(pc.paste())
    # gets content of clipboard, then prints it to console. 

main()