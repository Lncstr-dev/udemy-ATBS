# Adam Lancaster
# this program displays and manipulates the contents of the clipboard.
# for best results, copy something to the clipboard before running program,
# otherwise output will be inconsistent.

import pyperclip as pc

def main():

    clipboard = pc.paste()

    print(clipboard)

    pc.copy('this is a test message.')

    clipboard = pc.paste()

    print(clipboard)

main()