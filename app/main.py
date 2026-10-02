import os


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) != 3 or commands[0] != "mv":
        print("Invalid command!")
        return

    _, source_file, new_file_dest = commands

    if source_file == new_file_dest:
        print("Give me a new file!")
        return

    try:
        with open(source_file, "r") as f:
            input_text = f.read()
    except FileNotFoundError:
        print("Give me the source file!")
        return

    destination = new_file_dest.split("/")
    folders = destination[:-1]

    path = ""
    for folder in folders:
        path = os.path.join(path, folder)
        if not os.path.exists(path):
            os.mkdir(path)

    file_path = os.path.join(path, destination[-1])

    with open(file_path, "w") as f:
        f.write(input_text)

    os.remove(source_file)
