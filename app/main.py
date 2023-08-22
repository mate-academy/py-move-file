import os


def move_file(command: str) -> None:
    commands = command.split(" ")
    try:
        first_file = commands[1]
        second_file = commands[2]
    except IndexError:
        return
    if commands[0] != "mv" or first_file == second_file:
        return

    if os.path.dirname(second_file) != "":
        os.makedirs(os.path.dirname(second_file), exist_ok=True)

    with (open(first_file, "r") as read_file,
          open(second_file, "w") as write_file):
        write_file.write(read_file.read())
    os.remove(first_file)
