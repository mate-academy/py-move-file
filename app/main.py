import os


def move_file(command: str) -> None:
    command_name, file, path = command.split()

    if command_name != "mv":
        print("This command not exist")
        return

    if len(path.split("/")) > 1:
        os.makedirs("/".join(path.split("/")[:-1]), exist_ok=True)

    try:
        with (open(file, "r") as current_file,
              open(path, "x") as new_file):
            new_file.write(current_file.read())
        os.remove(file)
    except FileExistsError:
        return
