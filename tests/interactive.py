
import blessed
import ledcontrol

def on_select(x, y, val):
    val = int(val)
    myy = y
    myx = x
    if y<=4:
        if myy == 0:
            myy = 3
        elif myy == 1:
            myy = 2
        elif myy == 2:
            myy = 1
        elif myy == 3:
            myy = 0
        myx = x
        with open('queuecoords.txt', 'w') as file:
            # file.write("\n")
            file.write(str((myx, myy)) + 'libdbcc')
        ledcontrol.turnalldark()
        ledcontrol.highlight(myx,myy)
        return
    else:
        myy = y - 7
        myx = x
    if val == 32:
        myx = 0
        myy = 4
    elif val == 33:
        myx = 1
        myy = 4
    elif val == 34:
        myx = 0
        myy = 5
    elif val == 35:
        myx = 1
        myy = 5
    with open('queuecoords.txt', 'w') as file:
        # file.write("\n")
        file.write(str((myx, myy)) + 'libdb')
    ledcontrol.grid(myx, myy, "green")


def main():
    term = blessed.Terminal()

    cursor_y, cursor_x = 0, 0

    numbers = [
        ["10", "11", "12"],
        ["07", "08", "09"],
        ["04", "05", "06"],
        ['01', '02', '03'],
        [],
        [],
        [],
        ["00", "01", "02", "03", "04", "05", "06", "07"],
        ["08", "09", "10", "11", "12", "13", "14", "15"],
        ["16", "17", "18", "19", "20", "21", "22", "23"],
        ["24", "25", "26", "27", "28", "29", "30", "31"],
        ["32", "32", "32", "32", "33", "33", "33", "33"],
        ["34", "34", "34", "34", "35", "35", "35", "35"]
    ]

    text_lines = [
        "grid system                          \n----------------------"
    ]
    
    def draw_table():
        with term.location(0, 0):
            print(term.white("card catalog \n---------------------------\n-----"), end="\n")
        with term.location(0, 2):
            for y, row in enumerate(numbers):
                for x, num in enumerate(row):
                    if y == cursor_y and x == cursor_x:
                        print(term.on_black(term.white(num)), end="")
                    else:
                        print(term.white(num), end="")
                    print(" ", end="")
                print()
        with term.location(0, 7):
            for line in text_lines:
                print(term.white(line))

    def is_valid_position(y, x):
        return (0 <= y < len(numbers) and 0 <= x < len(numbers[y]) and numbers[y])

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)
            draw_table()

            key = term.inkey()

            if key.code == term.KEY_UP:
                new_y = cursor_y - 1
                while not is_valid_position(new_y, cursor_x) and new_y >= 0:
                    new_y -= 1
                if is_valid_position(new_y, cursor_x):
                    cursor_y = new_y

            elif key.code == term.KEY_DOWN:
                new_y = cursor_y + 1
                while not is_valid_position(new_y, cursor_x) and new_y < len(numbers):
                    new_y += 1
                if is_valid_position(new_y, cursor_x):
                    cursor_y = new_y

            elif key.code == term.KEY_LEFT:
                new_x = cursor_x - 1
                while not is_valid_position(cursor_y, new_x) and new_x >= 0:
                    new_x -= 1
                if is_valid_position(cursor_y, new_x):
                    cursor_x = new_x

            elif key.code == term.KEY_RIGHT:
                new_x = cursor_x + 1
                while not is_valid_position(cursor_y, new_x) and new_x < len(numbers[cursor_y]):
                    new_x += 1
                if is_valid_position(cursor_y, new_x):
                    cursor_x = new_x

            elif key == '\n' or key == ' ':
                on_select(cursor_x, cursor_y, numbers[cursor_y][cursor_x])
            elif key == 'q' or key == term.KEY_ESCAPE:
                break

if __name__ == "__main__":
    main()
