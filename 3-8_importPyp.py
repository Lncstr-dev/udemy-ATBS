# Adam Lancaster
# this program displays and manipulates the contents of the clipboard.
# for best results, copy something to the clipboard before running program,
# otherwise output will be inconsistent.

import pyperclip as pc

def main():

    pc.copy('this is the first message.')
    # this function copies the msg txt to clipboard.

    clipboard = pc.paste()
    # this function copies clipboard txt to variable.

    print(clipboard)
    # prints contents of clipboard.

    pc.copy('this is the second message.')

    clipboard = pc.paste()

    print(clipboard)

main()

