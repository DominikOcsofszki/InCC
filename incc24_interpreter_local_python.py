#! .venv/bin/python3

import argparse

from compiler import compiler
from interpreter import interpreter


def interpreter_file():
    argparser = argparse.ArgumentParser(
        prog="InCC24", description="CLI tool for the InCC24 language"
    )
    argparser.add_argument("file", type=str, nargs="?", help="The file to interpret")
    args = argparser.parse_args()
    if not args.file:
        print("File missing")
        exit()
    args.repl = False

    interpreter.main(args)


if __name__ == "__main__":
    interpreter_file()
