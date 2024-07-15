#!/usr/bin/env python3
from brain_games.games.prime import prime_game
from .utils import play_game


def main():
    play_game(prime_game, "prime")


if __name__ == '__main__':
    main()
