from Rename import Rename

rename = Rename()
while True:
    print("""
        1. new path
        2. start renaming
        q. exit
    """)

    match(input('> ')):
        case '1':
            rename.newPath()
        case '2':
            rename.rename()
        case 'q':
            break