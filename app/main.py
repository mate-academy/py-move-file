import os


def move_file(command: str) -> None:

    commands = command.split()

    if len(commands) != 3:
        return

    file1 = commands[1]
    file2 = commands[2].split("/")[-1]
    paths = commands[2].split("/")[:-1]

    create_path = ""

    for path in paths:
        create_path += path
        if not os.path.exists(create_path):
            os.mkdir(create_path)
        create_path += "/"

    with open(file1, "r") as f:
        text_file1 = f.read()

    with open(f"{create_path}{file2}", "w") as f:
        f.write(text_file1)

    os.remove(file1)
