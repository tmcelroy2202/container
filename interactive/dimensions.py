
from blessed import Terminal

def getdimensions():
    term = Terminal()
    width, height = 10, 10
    
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)

            for i in range(height+1):
                for j in range(width):
                    print(term.move_yx(i * 2, j * 2) + 'X')

            print(term.move_yx(0, 0) + "Use arrow keys to expand/shrink width and height")
            print(term.move_yx(1, 0) + "Press 'Enter' to finalize dimensions")

            key = term.inkey(timeout=0.05)

            if key.code == term.KEY_RIGHT:
                width += 1
            elif key.code == term.KEY_LEFT and width > 1:
                width -= 1
            elif key.code == term.KEY_UP and height > 1:
                height -= 1
            elif key.code == term.KEY_DOWN:
                height += 1
            elif key == '\n':
                print(term.home + term.clear)
                return width, height

if __name__ == "__main__":
    x, y = main()
    print(x, y)
