import random
import curses

# Constants
INITIAL_SNAKE_LENGTH = 3
SNAKE_HEAD_CHAR = curses.ACS_CKBOARD
FOOD_CHAR = curses.ACS_PI
TIMEOUT = 100

def create_initial_snake(screen_width, screen_height):
    snake_x = screen_width / 4
    snake_y = screen_height / 2
    return [[snake_y, snake_x - i] for i in range(INITIAL_SNAKE_LENGTH)]

def create_food(snake, screen_width, screen_height):
    food = None
    while food is None:
        new_food = [random.randint(1, screen_height - 1), random.randint(1, screen_width - 1)]
        food = new_food if new_food not in snake else None
    return food

def move_snake(snake, key):
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

def check_collision(snake, screen_height, screen_width):
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        return True
    return False

def update_screen(window, snake, food, ate_food):
    if not ate_food:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), " ")
    window.addch(int(snake[0][0]), int(snake[0][1]), SNAKE_HEAD_CHAR)
    if ate_food:
        window.addch(food[0], food[1], FOOD_CHAR)

def play_game():
    screen = curses.initscr()
    curses.curs_set(0)
    screen_height, screen_width = screen.getmaxyx()
    window = curses.newwin(screen_height, screen_width, 0, 0)
    window.keypad(1)
    window.timeout(TIMEOUT)

    snake = create_initial_snake(screen_width, screen_height)
    food = create_food(snake, screen_width, screen_height)
    window.addch(int(food[0]), int(food[1]), FOOD_CHAR)

    key = curses.KEY_RIGHT

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        if check_collision(snake, screen_height, screen_width):
            curses.endwin()
            quit()

        move_snake(snake, key)

        ate_food = snake[0] == food
        if ate_food:
            food = create_food(snake, screen_width, screen_height)

        update_screen(window, snake, food, ate_food)


def main():
    user_input = input("Do you want to play the snake game, type 'yes' or 'no': ").lower()
    if user_input == "yes":
        play_game()
    else:
        quit()

if __name__ == "__main__":
    main()
