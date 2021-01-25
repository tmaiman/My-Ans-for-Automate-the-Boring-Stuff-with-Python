#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw del <keyword> - delete keyword and its content.
# py.exe mcb.pyw del - deletes all keywords and their contents.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys
import pyinputplus as pyin
mcbShelf = shelve.open('mcb.save')

# Save/delete clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(f'Saved {sys.argv[2]} :\n{pyperclip.paste()}\ninto mcb.save file')
    elif sys.argv[1].lower() == 'del':
        try:
            del mcbShelf[sys.argv[2]]
            print(f'deleted {sys.argv[2]} from mcb.save file')
        except KeyError:
            print('No such key')
    
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'del':
        print('Deleting ALL keys in mcb.save file!')
        if pyin.inputYesNo(prompt='Are you sure?') == 'yes':
            for key in list(mcbShelf.keys()):
                del mcbShelf[key]
            print('\nDeleted all keys')
    else:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(' '.join(list(mcbShelf.keys())))
            print(f'Clipboard content:\n{pyperclip.paste()}')
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
            print(f'Clipboard content:\n{pyperclip.paste()}')
        else:
            print(f'{sys.argv[1]} is not in mcb.save')

mcbShelf.close()
