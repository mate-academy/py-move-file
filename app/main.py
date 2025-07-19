import os


def move_file(command: str) -> None:
    command_words = command.strip().split()

    if command_words[0] == "mv":
        try:
            os.rename(command_words[1], command_words[2])
        except FileNotFoundError:
            os.makedirs("/".join(command_words[2].split("/"))[:-1])
            os.rename(command_words[1], command_words[2])
