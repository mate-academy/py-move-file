import os


def move_file(command: str) -> None:
    commands = command.split()
    head = os.path.split(commands[2])[0]
    tail = os.path.split(commands[2])[1]
    if len(commands) != 3:
        raise ValueError("The command should contain the name of the command, "
                         "source file name, and directory to move")
    elif commands[0] != "mv":
        raise ValueError("The command should begin from 'mv'")
    elif head == "":
        os.rename(commands[1], commands[2])
    else:
        if not os.path.exists(head):
            os.makedirs(head)
        if tail == "":
            destination_path = os.path.join(head, commands[1])
        else:
            destination_path = commands[2]
        source_path = commands[1]
        with (
            open(source_path, "r") as source_file,
            open(destination_path, "w") as destinate_file
        ):
            content = source_file.read()
            destinate_file.write(content)
        os.remove(source_path)
