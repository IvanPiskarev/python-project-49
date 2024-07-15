#!/usr/bin/env python3
from brain_games.games.calc import calc_game
from .utils import play_game


def main():
    play_game(calc_game, "calc")


if __name__ == '__main__':
    main()
