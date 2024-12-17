import os


def move_file(command: str) -> None:
    instructions = command.split()

    if len(instructions) != 3 or instructions[0] != "mv":
        raise ValueError("Incorrect command")
    _, source, destination = instructions

    if os.path.exists(destination):
        raise FileExistsError("File already exists!")

    path = os.path.dirname(destination)
    new_name = os.path.basename(destination)

    if path and not os.path.exists(path):
        os.makedirs(path)
    if path:
        new_name = os.path.join(path, new_name)

    with open(source, "r") as old, open(new_name, "w") as new:
        new.write(old.read())

    os.remove(source)
