#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.even import generate_round

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
