#!/usr/bin/env python3
from brain_games.games.progression import progression_game
from .utils import play_game


def main():
    play_game(progression_game, "progression")


if __name__ == '__main__':
    main()
