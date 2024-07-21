
from blessed import Terminal

def goassign(width, height):
    term = Terminal()
    grid = [[0 for _ in range(width)] for _ in range(height)]
    cursor_x, cursor_y = 0, 0

    def draw_grid():
        for i in range(height):
            for j in range(width):
                print(term.move_yx(i * 2, j * 4) + f"{grid[i][j]:<4}")

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)

            draw_grid()

            print(term.move_yx(cursor_y * 2, cursor_x * 4) + term.reverse(f"{grid[cursor_y][cursor_x]:<4}"))

            print(term.move_yx(height * 2 + 1, 0) + "Use arrow keys to navigate, type number and press 'Enter' to assign")
            print(term.move_yx(height * 2 + 2, 0) + "Press 'q' to quit")

            key = term.inkey()

            if key.code == term.KEY_RIGHT and cursor_x < width - 1:
                cursor_x += 1
            elif key.code == term.KEY_LEFT and cursor_x > 0:
                cursor_x -= 1
            elif key.code == term.KEY_UP and cursor_y > 0:
                cursor_y -= 1
            elif key.code == term.KEY_DOWN and cursor_y < height - 1:
                cursor_y += 1
            elif key == 'q':
                break
            elif key.is_sequence and key.name == "KEY_ENTER":
                print(term.move_yx(height * 2 + 3, 0) + "Enter a number (up to 3 digits): ")
                user_input = ''
                while True:
                    num_key = term.inkey(timeout=10)
                    if num_key.is_sequence and num_key.name == "KEY_ENTER":
                        break
                    elif num_key.isdigit() and len(user_input) < 3:
                        user_input += num_key
                        print(num_key, end='', flush=True)
                    elif num_key.code == term.KEY_BACKSPACE and user_input:
                        user_input = user_input[:-1]
                        print(term.move_left + ' ' + term.move_left, end='', flush=True)
                
                if user_input.isdigit() and 0 <= int(user_input) <= 999:
                    grid[cursor_y][cursor_x] = int(user_input)
                else:
                    print(term.move_yx(height * 2 + 4, 0) + "Invalid input. Please enter a number between 0 and 999.")
                    term.inkey(timeout=2)  
    
    return grid

if __name__ == "__main__":
    # Example dimensions, replace with desired dimensions
    width, height = 10, 10
    final_grid = main(width, height)
    for row in final_grid:
        print(row)
