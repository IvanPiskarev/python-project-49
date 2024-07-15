#!/usr/bin/env python3
from brain_games.games.gcd import gcd_game
from .utils import play_game


def main():
    play_game(gcd_game, "gcd")


if __name__ == '__main__':
    main()
