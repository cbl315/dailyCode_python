#! usr/bin/env python
# 2016/12/25
import curses
from random import randrange, choice
from collections import defaultdict
from prettytable import PrettyTable


__author__ = 'blcai'

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letters_code = [ord(ch) for ch in 'WASDRQwasdrq']
action_dic = dict(zip(letters_code, actions*2))


def get_user_action(keyboard):
    char = 'zz'
    while(char not in action_dic):
        char = keyboard.getch()
    return action_dic[char]


def transpose(field):
    return [list(row) for row in zip(*field)]


def invert(field):
    return [row[::-1] for row in field]


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_score = win
        self.current_score = 0
        self.maxscore = 0
        self.reset()

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice(
            [(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0]
            )
        self.field[i][j] = new_element

    def reset(self):
        self.maxscore = (
            self.current_score if self.current_score > self.maxscore
            else self.maxscore)
        self.current_score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    def move(self, direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row)-len(new_row))]
                return new_row

            def merge(row):
                is_pair = False
                new_row = []
                for i in range(len(row)):
                    if is_pair:
                        new_row.append(2*row[i])
                        self.current_score += 2*row[i]
                        is_pair = False
                    else:
                        if i+1 < len(row) and row[i] == row[i+1]:
                            is_pair = True
                            new_row.append(0)  # next loop will append 2*row[i]
                        else:
                            new_row.append(row[i])
                assert(len(new_row) == len(row))
                return new_row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.is_move_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_score for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.is_move_possible(move) for move in actions)

    def is_move_possible(self, move):
        def can_row_left(row):
            def change(i):
                if row[i] == 0 and row[i+1] != 0:
                    return True
                if row[i] != 0 and row[i] == row[i+1]:
                    return True
                return False
            return any(change(i) for i in range(len(row)-1))

        check = {}
        check['Left'] = lambda field: any(can_row_left(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))

        if move in check:
            return check[move](self.field)
        else:
            return False

    # This function is not writted by myself
    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        
        def cast(string):
            screen.addstr(string + '\n')

        # 绘制水平分割线
        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()

        cast('SCORE: ' + str(self.current_score))
        if 0 != self.maxscore:
            cast('HGHSCORE: ' + str(self.maxscore))

        for row in self.field:
            draw_hor_separator()
            draw_row(row)

        draw_hor_separator()

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)


def main(stdscr):
    def init():
        game_field.reset()
        return 'Game'

    def not_game(stage):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)  # 默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'  # 对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        # 画出当前棋盘状态
        game_field.draw(stdscr)
        # 读取用户输入得到action
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):  # move successful
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    curses.use_default_colors()
    game_field = GameField(win=32)

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)
