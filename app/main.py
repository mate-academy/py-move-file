import os


def move_file(command: str) -> None:
    try:
        key, first_file, second_file = command.split()
    except IndexError:
        return
    if key != "mv" or first_file == second_file:
        return

    if os.path.dirname(second_file) != "":
        os.makedirs(os.path.dirname(second_file), exist_ok=True)

    with (open(first_file, "r") as read_file,
          open(second_file, "w") as write_file):
        write_file.write(read_file.read())
    os.remove(first_file)
