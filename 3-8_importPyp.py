# Adam Lancaster
# this program displays and manipulates the contents of the clipboard.

import pyperclip as pc

def main():
# main function loads the clipboard with a message, then prints the contents
# of the clipboard. it then repeats this process with the second message. 

    clipboardPnP('this is the first message.')
    clipboardPnP('this is the second message.')

def clipboardPnP(statement):
# clipboard paste and printer. I couldnt think of something better to call
# it, and clipboardPasteAndPrint is way too long. function loads statement 
# into clipboard then prints the contents of the clipboard.

    pc.copy(statement)
    # this function copies the msg txt to clipboard.
    clipboard = pc.paste()
    # this function copies clipboard txt to variable.
    print(clipboard)
    # prints contents of clipboard.

main()