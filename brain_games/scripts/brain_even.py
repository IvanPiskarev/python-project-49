#!/usr/bin/env python3
from brain_games.games.even import even_game
from .utils import play_game


def main():
    play_game(even_game, "even")


if __name__ == '__main__':
    main()
