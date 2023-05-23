import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3:
        raise ValueError("The command should contain the name of the command, "
                         "source file name, and directory to move")
    elif commands[0] != "mv":
        raise ValueError("The command should begin from 'mv'")
    elif commands[2].find("/") == -1:
        os.rename(commands[1], commands[2])
    else:
        if commands[2][-1] == "/":
            if not os.path.exists(commands[2]):
                os.makedirs(commands[2])
            destination_path = os.path.join(commands[2], commands[1])
        else:
            index = commands[2].rfind("/")
            destination = commands[2][:index + 1]
            if not os.path.exists(destination):
                os.makedirs(destination)
            destination_path = commands[2]

        source_path = commands[1]
        with (
            open(source_path, "r") as source_file,
            open(destination_path, "w") as destinate_file
        ):
            content = source_file.read()
            destinate_file.write(content)
        os.remove(source_path)
