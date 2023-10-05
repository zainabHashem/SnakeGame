import curses
import random

def main(stdscr):
    stdscr.clear()
    screen_h = 30
    screen_w = 90
    window = curses.newwin(screen_h + 1, screen_w + 1, 0, 0)
    curses.init_pair(1, curses.COLOR_GREEN,curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE)
    window.attron(curses.color_pair(2))
    window.border()
    window.attroff(curses.color_pair(2))
    window.keypad(True)
    vel = 100
    window.timeout(vel)
    score = 0
    window.addstr(0, int(screen_w * 0.8), "SCORE: {} ".format(score), curses.color_pair(1))
    snake_x = int(screen_w / 4)
    snake_y = int(screen_h / 2)

    snk = [
        (snake_y, snake_x),
        (snake_y, snake_x - 1),
        (snake_y, snake_x - 2)
    ]
    key = curses.KEY_RIGHT
    food = (int(screen_h/ 2), int(screen_w / 2))
    window.addch(food[0], food[1], "O")
    while True:
        new_head = None
        if snk[0][0] in (0, screen_h) or snk[0][1] in (0, screen_w) or snk[0] in snk[1:]:
            curses.endwin()
            print("GAME OVER")
            quit()
        next_key = window.getch()
        if next_key == -1:
            key = key
        else:
            key = next_key
        if key == ord('q'):
            break
        if key == curses.KEY_RIGHT or next_key == 454:
            new_head = (snk[0][0], snk[0][1] + 1)
        elif key == curses.KEY_LEFT or next_key == 452:
            new_head = (snk[0][0], snk[0][1] - 1)
        elif key == curses.KEY_UP or next_key == 450:
            new_head = (snk[0][0] - 1, snk[0][1])
        elif key == curses.KEY_DOWN or next_key == 456:
            new_head = (snk[0][0] + 1, snk[0][1])

        snk.insert(0, new_head)
        if snk[0] == food:
            food = None
            window.timeout(int(vel * 0.98))
            score += 1
            window.addstr(0, int(screen_w * 0.8), "SCORE: {} ".format(score), curses.color_pair(1))

            while food is None:
                new_food = (random.randint(1, screen_h - 1), random.randint(1, screen_w - 1))
                if new_food in snk:
                    new_food = None
                else:
                    food = new_food
            window.addch(food[0], food[1], "O")
        else:
            tail = snk.pop()
            window.addch(tail[0], tail[1], " ")
        window.addch(new_head[0],new_head[1], curses.ACS_BLOCK)

    print("GAME OVER")

curses.wrapper(main)