import os


def move_file(command: str) -> None:

    commands = command.split()

    if len(commands) != 3 or commands[0] != "mv":
        return

    file1 = commands[1]
    path_file = commands[2].split("/")

    create_path = ""

    for path in path_file[:-1]:
        create_path = os.path.join(create_path, path)
        if not os.path.exists(create_path):
            os.mkdir(create_path)

    with open(file1, "r") as f:
        text_file1 = f.read()

    with open(os.path.join(create_path, path_file[-1]), "w") as f:
        f.write(text_file1)

    os.remove(file1)
