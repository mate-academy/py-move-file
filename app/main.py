import os


def move_file(command: str) -> None:
    command = command.split()[1:]

    if "/" not in command[1]:
        os.rename(command[0], command[1])
        return None
    else:
        separate = command[1].split("/")
        os.makedirs("/".join(separate[:-1]))

        with open(command[0], "r") as current, \
                open(f"{command[1]}", "w") as out:

            for text in current.read():
                out.write(text)

    os.remove(command[0])
