import os


def move_file(command: str) -> None:
    instructions = command.split()
    _, source, destination = instructions

    if len(instructions) != 3 or instructions[0] != "mv":
        raise ValueError("Incorrect command")

    if os.path.exists(destination):
        raise FileExistsError("Already exists!")

    path = os.path.join("/".join(destination.split("/")[:-1]))
    new_name = destination.split("/")[-1]

    if path and not os.path.exists(path):
        os.makedirs(path)
    if path:
        new_name = os.path.join(path + "/" + new_name)

    with open(source, "r") as old, open(new_name, "w") as new:
        new.write(old.read())

    os.remove(source)
