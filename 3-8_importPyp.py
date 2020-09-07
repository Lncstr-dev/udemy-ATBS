# adam lancaster
# this program displays and manipulates the contents of the clipboard.
# for best results, copy something to the clipboard before running program.

import pyperclip as pc

def main():

    clipboard = pc.paste()

    print(clipboard)

    pc.copy('this is a test message.')

    clipboard = pc.paste()

    print(clipboard)

main()