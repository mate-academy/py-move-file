import os
import sys


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) == 3 and commands[0] == "mv":
        _, file, path_to_move = commands
        directories, filename = os.path.split(path_to_move)

        with open(file, "r") as r:
            content = r.read()

            if os.path.isdir(directories) or directories == "":
                with open(os.path.join(directories, filename), "a") as a:
                    a.write(content)
            else:
                os.makedirs(directories, exist_ok=True)
                with open(path_to_move, "a") as a:
                    a.write(content)

        os.remove(file)


if __name__ == "__main__":
    move_file(str(sys.argv))
