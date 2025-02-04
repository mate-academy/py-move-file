import os


def move_file(command: str) -> None:
    moving_file = command.split()[1]
    path = command.split()[-1]
    new_path = ""
    for i in range(len(path.split("/")) - 1):
        new_path = os.path.join(new_path, path.split("/")[i])
        os.makedirs(new_path, exist_ok=True)

    with open(moving_file, "r") as file, open(path, "w") as new_file:
        new_file.write(file.read())
    os.remove(moving_file)
